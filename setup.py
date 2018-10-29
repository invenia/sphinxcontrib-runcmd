import codecs

from setuptools import find_packages, setup

TEST_DEPS = ["coverage", "pytest", "pytest-cov", "sphinx_testing"]

EXTRAS = {"test": TEST_DEPS}

setup(
    name="sphinxcontrib-runcmd",
    version="0.1.3",
    author="Fernando Chorney",
    author_email="fernando.chorney@invenia.ca",
    url="https://github.com/invenia/sphinxcontrib-runcmd",
    download_url="https://pypi.org/project/sphinxcontrib-runcmd",
    license="MIT",
    description='Sphinx "runcmd" extension',
    long_description=codecs.open("README.md", "r", "utf-8").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=["sphinx"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ],
    platforms="any",
    test_require=TEST_DEPS,
    extras_require=EXTRAS,
    namespace_packages=["sphinxcontrib"],
)
