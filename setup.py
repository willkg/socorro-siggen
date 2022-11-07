#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import codecs
import os
import re

from setuptools import setup, find_packages


def get_long_desc():
    return codecs.open("README.rst", encoding="utf-8").read()


def get_version():
    fn = os.path.join("siggen", "__init__.py")
    vsre = r"""^__version__ = ['"]([^'"]*)['"]"""
    version_file = codecs.open(fn, mode="r", encoding="utf-8").read()
    return re.search(vsre, version_file, re.M).group(1)


INSTALL_REQUIRES = [
    "glom",
    "importlib_resources",
]
EXTRAS_REQUIRE = {
    "cli": [
        "requests<3",
    ],
}


setup(
    name="siggen",
    version=get_version(),
    description="Experimental extraction of Socorro signature generation",
    long_description=get_long_desc(),
    long_description_content_type="text/x-rst",
    maintainer="Will Kahn-Greene",
    maintainer_email="willkg@mozilla.com",
    url="https://github.com/willkg/socorro-siggen",
    license="Mozilla Public License v2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=3.7",
    entry_points="""
        [console_scripts]
        signify=siggen.cmd_signify:main
        fetch-data=siggen.cmd_fetch_data:main
        signature=siggen.cmd_signature:main
    """,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
