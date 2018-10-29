# SphinxContrib RunCmd

[![Build Status](https://travis-ci.org/invenia/sphinxcontrib-runcmd.svg?branch=master)](https://travis-ci.org/invenia/sphinxcontrib-runcmd?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/invenia/sphinxcontrib-runcmd/badge.svg?branch=master)](https://coveralls.io/github/invenia/sphinxcontrib-runcmd)
[![Pip Version](https://img.shields.io/pypi/v/sphinxcontrib-runcmd.svg)](https://pypi.org/project/sphinxcontrib-runcmd)
[![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Sphinx RunCmd aims to allow you to place the output of arbitrary commands in your rst files, while also giving you greater flexibility in how the output is formatted.

## Installation

sphinxcontrib-runcmd is available on PyPI. To install:

```sh
$ pip install sphinxcontrib-runcmd
```

## Add runcmd to your Project

First you'll want to add `sphinxcontrib.runcmd` to your `conf.py` file in your docs folder:

```python
extensions = ["sphinxcontrib.runcmd"]
```

From there, all you need to do is use `runcmd` as a directive in your documentation files.
```rst
.. runcmd:: python script.py -h
   :syntax: bash
   :prompt:
```

## Options

This directive is basically a sub-directive of `code-block`, so it has all of code blocks directives such as:
 - linenos
 - dedent
 - lineno-start
 - emphasize-lines
 - caption
 - class
 - name

This directive builds upon that and adds the following:
 - syntax: str
  - Since we're using the arguments section for a command we can't actually pass the syntax we want to the `code-block` in the arguments. Therefore you can set it in the options which will then get passed into the `code-block` to colorize your commands output.
 - replace: str
  - Takes in a comma separated list of regex `pattern/replace,pattern/replace` and applies it to the output in that order.
 - prompt: bool
  - Display the command prompt in the output
 - dedent-output: int
  - Will dedent the output only by the int value you specify. Will not dedent the prompt if specified. Be careful, because the `code-block` dedent will be applied on top of this dedent if both are set in the options.

### Replace Option

The `replace` option uses the `CSV` package to parse the string, thus you can wrap your replacements in double quotes if you want to use commas and whatnot.

You also need to double escape any forward slashes, but you can single escape quotes.

```rst
.. runcmd:: python test.py -h
  :replace: "this\\/is\\/a\\/path/now\\/its\\/another\\/path","\"/'"
```

The first replacement will replace `this/is/a/path` with `now/its/another/path`.

The second replacement will replace `"` with `'`.

## License

sphinxcontrib-runcmd is provided under an MIT License.
