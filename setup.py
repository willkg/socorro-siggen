#!/usr/bin/env python

from setuptools import setup, find_packages


install_requires = [
    'glom',
    'requests',
    'ujson',
]


setup(
    name='siggen',
    version='0.1',
    description='Experimental extraction of Socorro signature generation',
    maintainer='Will Kahn-Greene',
    maintainer_email='willkg@mozilla.com',
    url='https://github.com/willkg/socorro-siggen',
    license='Mozilla Public License v2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points="""
        [console_scripts]
        signify=siggen.cmd_signify:cmdline
        fetch-data=siggen.cmd_fetch_data:cmdline
    """,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
    ]
)
