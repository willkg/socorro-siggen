=======
History
=======

1.0.0 (May 23rd, 2019)
======================

Bug fixes:

* 1553665: Add libc to the irrelevant signatures list.
* 1544246: add "fix_missing_module" pass to signature generation
* 1550028: Switch to crash-stats.mozilla.org
* 1544449: Fix NoteXPCOMChild class name.
* Update docs
* 1541090: add __clear_cache to prefix list
* 1541474: add real_drop_in_place to prefix list
* Add MessageLoop::PostTask and MessageLoop::PostTask_Helper to skip list (#4831)
* 1523968: add trunc to prefix list
* Add gkrust_shared::oom_hook::hook to the prefix list.
* 1520615: add schedule_class_load and SkyLight to irrelevant list
* Add alloc::raw_vec::capacity_overflow to the prefix list
* Drop support for Python 2.7 and 3.4
* Add Code of Conduct and links


0.2.1 (January 4th, 2019)
=========================

Bug fixes:

* Add support for Python 3.4, 3.5, and 3.6.
* 1515772: Add alloc::alloc::handle_alloc_error to the irrelevant signature list
* 1515487: slim down dll handling in signature generation
* 1515487: add ntdll.dll and friends to prefix list
* 1511022: add debug logging for signature generation
* 1511022: rework signature generation to use a Result instance
* 1514746: add std::panicking::begin_panic<T> to sentinels
* 1507186: get all the webapp tests passing
* 1505954: add core::panicking::panic_fmt to sentinels
* 1505954: Add core::panicking::panic_bounds_check to the setinel list
* 1506781: fix silent ujson errors
* 1506228: fix socorro/unittest/cron tests to work in python 3
* 1503966: Add mozilla::detail::HashTable to the prefix list
* 1502477: add moz_crash_reason_raw
* 1501291: add nsTSubstring<T>::Assign to prefix list
* 1500401: add core::panicking::panic to sentinel list
* Update docs
* 1495966: add core::ptr::drop_in_place to prefix signature list (#4629)
* 1496732: add mbrtoc32 to prefix list
* 1496599: Clean up JavaStackTrace field
* Replace fake example with the real problematic string
* 1493200: fix an infinite loop
* 1493200: fix the double-clone vexing variation
* 1488774: fix another cause of & signatures
* 1493200: fix empty string signature generation
* 1488774: remove cv/ref qualifiers in function names


0.2.0 (August 29th, 2018)
=========================

Big changes:

* Siggen is re-united with Socorro's signature generation system. Generally
  we'll make changes in the Socorro repository and then copy them here.

Bug fixes:

* 1477726: add ``std:alloc::rust_oom`` to prefix list
* 1481282: rework frame normalization so it treats C/C++ frames differently
  than Rust frames
* 1477013: rewrite collapse to correctly handle Rust trait methods
* 1478383: drop prefix and return type in function signatures; add handling
  for "const" in function signatures
* 1306643: document signature generation pipeline


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
