==============
socorro-siggen
==============

This is an experimental extraction of the Socorro signature generation code.

:Code:          https://github.com/willkg/socorro-siggen
:Documentation: Check the README
:Issue tracker: https://github.com/willkg/socorro-siggen/issues
:License:       MPLv2
:Status:        Alpha


Installing
==========

socorro-siggen is available on `PyPI <https://pypi.org>`_. You can install it
with::

    $ pip install socorro-siggen


Basic use
=========

You can use socorro-siggen as a command line::

    $ siggen JSONFILE
    SIGNATURE HERE


You can use socorro-siggen as a library::

    from siggen import SignatureGenerator

    generator = SignatureGenerator()

    crash_data = {
    }

    ret = generator.generate(crash_data)
    print(ret['signature'])
