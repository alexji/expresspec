#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages
from codecs import open
from os import path, system
from re import compile as re_compile

# For convenience.
if sys.argv[-1] == "publish":
    system("python setup.py sdist upload")
    sys.exit()

def read(filename):
    kwds = {"encoding": "utf-8"} if sys.version_info[0] >= 3 else {}
    with open(filename, **kwds) as fp:
        contents = fp.read()
    return contents

# Get the version information.
here = path.abspath(path.dirname(__file__))
vre = re_compile("__version__ = \"(.*?)\"")
version = vre.findall(read(path.join(here, "expresspec", "__init__.py")))[0]

setup(
    name="expresspec",
    version=version,
    author="Alex Ji",
    #author_email="",  # <-- Direct complaints to this address.
    description="EXPRES",
    long_description=read(path.join(here, "README.md")),
    url="https://github.com/alexji/expresspec",
    license="MIT",
    keywords="astronomy",
    packages=find_packages(exclude=["documents", "tests"]),
    install_requires=[
        "numpy","astropy","scipy",
        ],
    extras_require={
        #"test": ["coverage"]
    },
    package_data={
        "": ["LICENSE"]
    },
    include_package_data=True,
    data_files=None,
    entry_points=None
)
