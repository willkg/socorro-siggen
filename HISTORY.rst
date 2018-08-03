=======
History
=======

0.1.3 (August 3rd, 2018)
========================

Bug fixes:

* Unified siggen fork with Socorro signature generator. Siggen is now an
  extracted library from Socorro's signature generator.

* Add tests for signature generator error handler.

* Some minor changes for Python 3 support.

* Other minor fixes.


0.1.2 (July 26th, 2018)
=======================

Bug fixes:

* Generalized code so it can be ignorant of parent module. This will make it
  easier to co-exist with Socorro's fork.

* Update signature lists with changes in Socorro over the last month.

* Cleanup README to make the schema easier to read. (Thank you, Ben!)

* Fix bugs and typos in examples.


0.1.1 (June 28th, 2018)
=======================

Bug fixes:

* Bug fixes related to differences in signature output between Socorro
  and siggen. This resulted in a couple of really minor schema changes:

  * "crashing_thread" now defaults to None indicating that no crashing
    thread was specified
  * "additional_minidumps" is now a text which has a comma-separated
    string value

  Issues #7 and #10.

* Added "original_signature" key to the JSON output of fetch-data command.

* Removed use of the logging module.


0.1.0 (June 27, 2018)
=====================

* Initial release
