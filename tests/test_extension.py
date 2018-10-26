from sphinx_testing import with_app


@with_app(buildername="html", srcdir="./tests/examples", copy_srcdir_to_tmpdir=True)
def sphinx_build(app, status, warning):
    app.build()
    with open(app.outdir + "/index.html", "r") as f:
        html = f.read()
    assert "python test.py -h" in html
    assert "No such file or directory" in html


def test_build():
    sphinx_build()
