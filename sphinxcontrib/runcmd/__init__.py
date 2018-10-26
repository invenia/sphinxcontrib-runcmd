import csv
import re
import shlex
import subprocess
import sys

from docutils.parsers.rst import directives
from sphinx.directives import code

from .utils import Singleton

__version__ = "0.1.0"

# CONSTANTS
RE_SPLIT = re.compile(r"(?P<pattern>.*)(?<!\\)/(?P<replacement>.*)")


class CMDCache(object, metaclass=Singleton):  # noqa: E999
    __metaclass__ = Singleton
    cache = {}

    def get(self, cmd):
        h = hash(cmd)
        if h in self.cache:
            return self.cache[h]
        else:
            result = run_command(cmd)
            self.cache[h] = result
            return result


def run_command(command):
    true_cmd = shlex.split(command)
    try:
        result = subprocess.run(
            true_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    except Exception as e:
        out = ""
        err = e
    else:
        encoding = sys.getfilesystemencoding()
        out = result.stdout.decode(encoding, "replace").rstrip()
        err = result.stderr.decode(encoding, "replace").rstrip()

    if err and err != "":
        print("Error in runcmd: {}".format(err))
        out = "{}\n{}".format(out, err)

    return out


class RunCmdDirective(code.CodeBlock):
    has_content = False
    final_argument_whitespace = False
    required_arguments = 1
    optional_arguments = 99

    option_spec = {
        # code.CodeBlock option_spec
        "linenos": directives.flag,
        "dedent": int,
        "lineno-start": int,
        "emphasize-lines": directives.unchanged_required,
        "caption": directives.unchanged_required,
        "class": directives.class_option,
        "name": directives.unchanged,
        # RunCmdDirective option_spec
        "syntax": directives.unchanged,
        "replace": directives.unchanged,
        "prompt": directives.flag,
        "dedent-output": int,
    }

    def run(self):
        # Grab a cache singleton instance
        cache = CMDCache()

        # Get the command output
        command = " ".join(self.arguments)
        output = cache.get(command)

        # Grab our custom commands
        syntax = self.options.get("syntax", "text")
        replace = self.options.get("replace", "")
        reader = csv.reader([replace], delimiter=",", escapechar="\\")
        prompt = "prompt" in self.options
        dedent_output = self.options.get("dedent-output", 0)

        # Dedent the output if required
        if dedent_output > 0:
            output = "\n".join([x[dedent_output:] for x in output.split("\n")])

        # Add the prompt to our output if required
        if prompt:
            output = "{}\n{}".format(command, output)

        # Do our "replace" syntax on the command output
        for items in reader:
            for regex in items:
                if regex != "":
                    match = RE_SPLIT.match(regex)
                    p = match.group("pattern")
                    # Let's unescape the escape chars here as we don't need them to be
                    # escaped in the replacement at this point
                    r = match.group("replacement").replace("\\", "")
                    output = re.sub(p, r, output)

        # Set up our arguments to run the CodeBlock parent run function
        self.arguments[0] = syntax
        self.content = [output]
        node = super().run()

        return node


def setup(app):
    app.add_directive("runcmd", RunCmdDirective)

    return {"version": __version__}
