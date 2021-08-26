#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

setuptools.setup(
    name = "ripe-api",
    version = "0.3.0",
    author = "Platforme International",
    author_email = "development@platforme.com",
    description = "RIPE API",
    license = "Apache License, Version 2.0",
    keywords = "ripe api",
    url = "http://www.platforme.com",
    zip_safe = False,
    packages = [
        "ripe"
    ],
    package_dir = {
        "" : os.path.normpath("src")
    },
    install_requires = [
        "appier"
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
