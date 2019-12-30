=======
History
=======

1.0.1 (December 30th, 2019)
===========================

Bug fixes:

* Bug 1604605 - Add IPDL write signatures to irrelevant list
* Remove IPDL write stuff from prefix list
* bug 1602344: add ``__forwarding_prep_0___`` to prefix list
* bug 1602343: adding ``___forwarding___`` to prefix list
* bug 1602342: add ``-[NSObject doesNotRecognizeSelector:]`` to prefix list
* bug 1601223: add ``moz_malloc_size_of`` to prefix list
* bug 1599779: support other crashid forms in signature command
* bug 1600951: add ``AllocInfo::Get<T>`` to prefix list
* bug 1599506: add ``NXMapRemove`` to prefix list
* Bug 1599222 - ``mozilla::ipc::IPDLParamTraits<T>::Write`` to the prefix signature list
* bug 1599168: add ``unlink`` to prefix list
* bug 1599167: add ``__unlink`` to prefix list
* bug 1599164: add ``__ulock_wait`` to prefix list
* bug 1599162: add ``__semwait_signal`` to prefix list
* bug 1599157: add ``__cxxabiv1::failed_throw`` to prefix list
* bug 1599165: add ``pthread_cond_signal_thread_np`` to prefix list
* bug 1599156: add ``CALayerRelease`` to prefix list
* bug 1599155: add ``CALayerRetain`` to prefix list
* bug 1599152: add ``objc_retain`` to prefix list
* bug 1599151: add ``objc_terminate`` to irrelevant list
* bug 1599149: add ``std::terminate`` to irrelevant list
* bug 1599147: add ``objc_exception_rethrow`` to prefix list
* bug 1599146: add ``__cxa_rethrow to irrelevant`` list
* bug 1599019: fix prefix changes to only add ``NSApplication``
* bug 1599019: add ``NSApplication`` functions to prefix list
* bug 1539305: update to python 3.7.5
* bug 1594665: add ``__pthread_mutex_lock`` to prefix list
* bug 1594468: move ``libc*`` lines from irrelevant list to prefix list
* bug 1592208: add more c functions to prefix list
* bug 1590194: add ``mozilla::MozPromise<T>::ThenInternal`` to prefix list
* bug 1590096: add more ``libc`` functions to prefix list
* bug 1589604: add ``gsignal`` and friends to prefix list
* bug 1588675: add ``strcmp`` implementation variations to prefix list
* bug 1584951: add ``memset`` implementation variations to prefix list
* bug 1584615: add ``objc_msgLookupSuper2`` to irrelevant list
* bug 1581800: add ``__memcpy.*`` to prefix list
* bug 1581800: add ``__memcpy_sse2_unaligned_erms`` to prefix list
* bug 1581517: add wayland symbols to prefix list
* bug 1567990: fix goofy things from black reformatting
* bug 1567990: reformat ``socorro/`` with black
* bug 1561697: add ``mozilla::ipc::WriteIPDLParam`` to prefix list
* bug 1557012: add ``Allocator<T>::malloc`` to prefix list
* Add ``BaseAllocator`` to the prefix signature list
* Add support for Python 3.8
* Fix Python 3.5 syntax issue
* Fix bugs in signify command line


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
