=======
History
=======

2.2.20241029 (October 29th, 2024)
=================================

Bug fixes:

* Drop support for Python 3.8. (#137)
* Add support for Python 3.13. (#136)
* bug 1926077: remove enclosing square bracket(s) from module name in signature generation (#6766)  (Bianca Danforth)
* Bug 1914848 - Ignore the functions in libdspatch when generating crash signatures  (Gabriele Svelto)
* Fix signature generation docs  (Will Kahn-Greene)


2.1.20240726 (July 26th, 2024)
==============================

Bug fixes:

* bug 1907894 - Add ``mozilla::Atomic<T>`` to the irrelevant signature list.
* Bug 1906667 - Add ``mozilla::media::Interval<T>`` to the prefix list. (#6663)
* Bug 1905714 - Only ``match JS::Call`` exactly in signatures. (#6652)
* bug-1904528: add ``SafeVariantClear`` and ``VariantCopy`` to prefix list
* bug-1904528: Update ``prefix_signature_re.txt``
* Update ruff to 0.5.0
* bug-1885919: Fix signature generation tests
* bug-1885919: add ``IPC::ReadParam`` to irrelevant list
* bug-1885919: add ``IPC::`` to pick up all IPC frames in signatures
* Bug-1885919 - Add ``IPC::MessageReader::FatalError`` to sentinels list
* Bug 1905094 - Improve signatures for JS context checks.
* Bug 1903022 - Add ``Variant`` to the prefix list and ``VariantImplementation`` to the irrelevant list.
* bug-1900995: remove ``SignatureParentIDNotEqualsChildID`` rule
* bug-1898268: Some updates to the docs for signature generation changes. (#6624)
* Bug 1860947 - Add ``ReleaseData`` and string buffer ``AddRef`` and ``Release`` methods to the irrelevant signature list (#6622)
* bug-1895527: fix ``normalize_frame`` docstring
* bug-1895527: remove extranneous paragraph and fix irrelevant/prefix lines
* bug-1895527: remove addresses from signatures


2.1.20240412 (April 12th, 2024)
===============================

Bug fixes:

* bug-1889120: add Rust sub-slice access frames to prefix signature list
* Bug 1885351 - Add ``nsCOMPtr<T>:: and nsMaybeWeakPtr<T>::`` to the irrelevant signature list.
* Bug 1884689 - Add ``nsDocShell::GetBrowsingContext`` to the prefix list.
* Bug 1882088 - Move ``nsTArray`` OOM things to the irrelevant list.
* bug-1850981: update to python 3.11
* bug-1876623: Treat ``<.plt ELF section...>`` as prefix signature
* bug-1799125: switch from ``urlparse`` from ``urllib.parse`` to ``urlsplit``
* Bug 1866857 - Ignore ``mozilla::Monitor::Lock`` when generating crash signatures
* Bug 1862460 - Add ``mozilla::Vector<T>`` to the prefix list.


2.0.20231009 (October 9th, 2023)
================================

Big changes:

* bug 1847429: implement signature generation for ``JavaException``
* Drop support for Python 3.7 (#109)

Bug fixes:

* bug 1847429: protect against frames being None
* bug 1847429: add schema docs for the crash data structure
* bug 1826703: add "hang" to ``convert_to_crash_data``
* Bug 1826703 - Add specific signatures for hung processes
* Bug 1850325 - Ignore ``<std::collections::hash::map::HashMap<K, V, S> as core::ops::index::Index<&Q>>::index`` when generating crash signatures
* Bug 1848162 - add ``mozilla::Span<T>`` as substring to ignore for signature generation
* Bug 1845173 - Add ``SegmentedVector`` to the prefix list
* bug 1845173 - add ``~nsCOMPtr`` and ``SegmentImpl`` to irrelevant list
* Bug 1845406 - Add ``nsTArrayElementTraits`` to the irrelevant signature list
* bug 1838201: add ``mozilla::CheckedInt`` to the prefix list
* bug 1834536: add ``mozilla::dom::syncedcontext::Transaction<T>::Commit`` to prefix list
* Update signature generation docs
* Bug 1831836 - Improve rust panic crash signatures
* Add dependabot to github actions
* Add support for Python 3.12 (#110)


1.1.20230418 (April 18th, 2023)
===============================

Bug fixes:

* Switch from flake8 to ruff (#106)
* Bug 1819178 - Add ``nsStringBuffer::`` to prefix list
* Bug 1827660 - Add ``do_AddRef`` to the irrelevant list
* bug 1827480: add ``Gecko_AppendCString`` to prefix list
* bug 1799528: fix bugbear issues
* Bug 1795651 - Ignore operations on hash tables and maps when generating a
  crash signature
* Bug 1824981 - Ignore some of the implementation details of the Rust
  ``Result<>`` type when generating a signature
* Add ``std::alloc::_::__rg_oom`` to irrelevant_signature_re.txt
* Bug 1822931 - Fix constant reference qualifiers in signatures
* Bug 1821453 - Ignore array iterator methods and the ``std::all_of()``
  function when generating a crash signature
* Bug 1821641 - Ignore functions used to store crash annotations, manipulate
  POD objects and write objects via IPC
* Bug 1819065 - Ignore several helpers, getters and constructors related to
  launching runnables when generating crash signatures
* Bug 1819062 - Ignore equality operators when generating crash signatures
* Bug 1816846 - Ignore various methods related to locks and promises to shorten
  signatures and peel apart different crashes
* bug 1815235: stringify cond names in SignatureShutdownTimeout rule
* Bug 1814563 - Ignore some getters in media code when generating the crash
  signature
* Bug 1811094 - Ignore thread-local storage getters when generating the crash
  signature
* Bug 1810971 - Ignore several inlined functions from the ``MozPromise`` class
* Bug 1810519 - Ignore all functions starting with ``__futex_abstimed_wait``
* Bug 1809847 - Add rust enum methods and others to the list of irrelevant
  functions
* bug 1806119: add ``nsQueryObject<T>::operator`` to irrelevant list
* Bug 1806107 - Improve Linux shutdown hang signatures
* Switch to using ``contextlib.suppress``
* bug 1796094: fix ``JSLargeAllocationFailure`` OOM detection
* Bug 1795631 - Ignore the ``RefPtr`` class and its helpers in signature
  generation
* Bug 1800132 - Tweaked signature generation for WebRTC crashes
* bug 1796094: mark ``JSLargeAllocationFailure=Reported`` as ``OOM | large``
* Bug 1804025 - Ignore functions used to access slices and vectors in Rust when
  generating the crash signature
* bug 1802715: add ``new[]`` to prefix list
* Update ``socorro/signature/siglists/prefix_signature_re.txt``
* Bug 1802315 - add ``mozilla::dom::Promise::*`` as signature prefix
* Bug 1801623 - Ignore worker-related functions during crash signature
  generation
* Bug 1801603 - Ignore some functions manipulating JS objects when generating
  crash signatures
* Bug 1801043 - Ignore various core rust functions when generating the crash
  signature
* Bug 1800460 - Ignore ``mozilla::ThreadSafeAutoRefCnt`` when generating crash
  signatures


1.1.20221108 (November 8th, 2022)
=================================

Bug fixes:

* Add --signature-list-dir argument to ``signify`` and ``signature`` commands.
  Add ``signature_list_dir`` argument to ``SignatureGenerator``. This allows
  you to specify an alternate directory for signature lists. (#75)
* Add support for Python 3.11 (#98)
* bug 1784866: remove ``pkg_resources``
* Bug 1799433 - ``Ignore mozilla::UniquePtr<T>`` functions when generating a crash signature
* bug 1799142: handle unsupported ``AsyncShutdownTimeout`` values
* bug 1796389: add "stackoverflow" to signature
* bug 1798495: add ``mozilla::Atomic<T>::Atomic`` to irrelevant list
* Bug 1798495 - Ignore Android atomics and more functions from STL implementations when generating signatures
* bug 1798480: add ``_guard_dispatch_icall_nop`` to irrelevant list
* Bug 1798480 - Ignore ``guard_dispatch_icall_nop`` when generating a crash signature
* Fix bad string interpolation in signature command
* Bug 1798479 - Ignore the functions under ``mozilla::detail::IntrinsicMemoryOps`` when generating a signature
* Disambiguate crashes that happen in ``mozilla::TimeStampValue::operator-``
* bug 1746630: use unloaded modules in signature generation
* bug 1795643: add ``nsINode::GetParentNode`` to prefix list
* bug 1795641: add ``nsObserverService`` to prefix list
* Bug 1794587 - Ignore most wait functions that appear in shutdown hang stacks
* Bug 1794362 - Add ``core::sync::atomic::`` to the irrelevant list
* Bug 1792710 - Added ``mozilla::Maybe<T>`` to the prefix list
* Bug 1791509 - Improve handling inlined library functions
* Add ``mozilla::OffTheBooksMutex::Lock`` to prefix list
* Add ``alloc::alloc::handle_alloc_error`` to sentinals
* Add ``enum$<T>::unwrap`` to prefix list
* Also add ``core::slice::index::slice_end_index_len_fail_rt``
* Add ``core::slice::index::slice_end_index_len_fail`` to the prefix list
* bug 1733904: fix comments from bad copypasta
* bug 1745732: improve signatures for crash reports with thread index issues
* bug 1788269: add inline functions to signature
* Bug 1790051 - Streamline the irrelevant signatures on Linux, macOS and Windows


1.0.20220909 (September 9th, 2022)
==================================

Bug fixes:

* Removed ``siggen.__releasedate__``. We'll include the date in the versions going
  forward.
* Moved dev requirements into ``requirements-dev.txt`` file.
* Fix signify to convert processed crash (#91)
* Fix fetch-data TypeError (#90)
* Switch to calver (#95)
* bug 1787933: exorcise flash from the codebase
* bug 1733904: add "bad hardware" to signature for ``STATUS_DEVICE_DATA_ERROR``
* Bug 1784464 - Add Android's compiler builtin functions to the irrelevant
  function list


1.0.9 (August 2nd, 2022)
========================

Bug fixes:

* bug 1764570: update to fillmore 0.1.1; drop ``capture_error``
* Bug 1777954 - Adjust regular expressions matching Android, Linux and macOS
  libraries that changed
* Bug 1777954 - Removed obsolete entries in the prefix and irrelevant lists
* Bug 1777954 - Reorganize signatures containing implementations of common
  library functions
* bug 1774110: add ``mozilla::dom::AutoJSAPI::Init`` to prefix list
* bug 1767279: fix license headers in python files


1.0.8 (December 6th, 2021)
==========================

Bug fixes:

* Removed ``siggen.VERSION``. Use ``siggen.__version__`` instead. (#83)
* Remove ujson and six dependencies (#80)
* Remove requests dependency by default. You'll need to install the ``cli``
  extras which cover installing required dependencies for scripts. (#80)

  ::

     pip install 'siggen[cli]'
  
* bug 1743487: remove ``total_frames`` from socorro
* bug 1737691: skip processing for 0-byte dump files
* bug 1741764: add ``RaiseFailFastException`` to prefix list
* bug 1737691: add new ``MinidumpStackwalkRule``
* bug 1737878: return normalized frames in signature result


1.0.7 (October 18th, 2021)
==========================

Bug fixes:

* bug 1733907: add glib functions to irrelevant list
* bug 1733910: add ``ERROR_NOT_ENOUGH_MEMORY`` as OOM indicator
* bug 1732662: add ``mozilla::detail::InvalidArrayIndex_CRASH`` to prefix list
* bug 1731972: add ``__GI___pthread_mutex_lock`` to irrelevant list
* bug 1727149: back out shutdownkill signature changes
* bug 1728738: add windows guard stack functions to irrelevant list
* bug 1730463: add ``mozilla::widget::WlCrashHandler`` to irrelevant list
* bug 1723474: look at reason for OOM indicator
* bug 1723465: add more windows symbols to irrelevant list
* bug 1716611: add pthreads_kill to prefix list
* bug 1715747: add Windows fastfail frames to irrelevant list
* bug 1716742: mark ``last_error_value`` ``ERROR_COMMITMENT_LEVEL`` as OOM
* bug 1720162: fix error in signature command
* Bug 1715634 - add ``get_fpsr`` to the irrelevant signature list
* Add support for Python 3.10 (#74)


1.0.6 (April 22nd, 2021)
========================

Bug fixes:

* Add ``__repr__`` to Result class (#68)
* Drop support for Python 3.6 (#70)
* bug 1706075: add Windows functions to prefix list
* bug 1699492: fix mutation issues in signature generation
* bug 1705027: add ``NS_CycleCollectorSuspect3`` to prefix list
* bug 1702984: add ``std::vector<T>::_Emplace_reallocate<T>`` to the prefix list


1.0.5 (March 18th, 2021)
========================

Bug fixes:

* Add markdown format to signature generation cli
* bug 1696363: add ``env_logger`` bits to irrelevant list
* bug 1692983: remove ``mozilla::detail::MutexImpl::unlock`` from sentinels
* bug 1694894: add glib assertion bits to irrelevant list
* pyupgrade pass
* bug 1687907: add more ``mozilla::detail::MutexImpl::`` sentinels
* Fix error handling in signature cmd
* Bug 1690034: add ``_rust_alloc_error_handler`` to irrelevant list
* Bug 1690034 - Add Rust OOM stuff to the irrelevant signature list.
* bug #1688249: remove lambda number from signature
* bug 1687907: add ``mozilla::detail::MutexImpl::mutexLock`` to sentinels
* bug 1685178: fix signature generation for unknown in dll frames
* Force ``crashing_thread`` to be an int
* bug 1681347: fix Linux assertion crash signatures
* bug 1672847: normalize anonymous namespace variations


1.0.4 (December 3rd, 2020)
==========================

Bug fixes:

* Add support for Python 3.9 (#55)
* Drop support for Python 3.5 (#54)
* bug 1676900: add ``std::io::stdio::_eprint`` to irrelevant list
* bug 1672386: add ``nsTSubstring<T>::Append`` to prefix list
* bug 1668381: add ``_XReply`` to irrelevant list
* bug 1667734: add frames to irrelevant and prefix lists
* bug 1667741: add Windows heap failure error handling to irrelevant list
* bug 1665791: add ``mozilla::UniquePtr<T>::reset`` to the prefix list
* bug 1667335: add ``std::_Func_impl_no_alloc<T>::_Do_call`` to the prefix list
* bug 1662720: add ``*$VARIANT$*`` symbols to irrelevant list
* bug 1660050: add ``NS_QuickSort`` to prefix list
* bug 1658729: add ``mozilla::TaskController::GetRunnableForMTTask`` to the prefix list
* bug 1651336: add ``mozilla::detail::nsTStringRepr<T>::`` to prefix list
* bug 1649774: add ``mozilla::detail::nsTStringRepr<T>::Equals`` to prefix list
* bug 1646675: add ``FindElementCommon`` to prefix list
* bug 1644234: add ``libart.so`` to prefix list
* bug 1640942: improve rust OOM signatures


1.0.3 (May 22nd 2020)
=====================

Bug fixes:

* bug 1633473: add ``pthread_mutex_trylock`` to prefix list
* bug 1383113: switch mozilla rules to getitem notation
* bug 1629854: add ``core::result::unwrap_failed`` to prefix list
* bug 1626801: add ``RpcpRaiseException`` to prefix list
* bug 1626801: move ``CxxThrowException`` to prefix list
* bug 1626801: add ``CxxThrowException`` and friends to sig lists
* bug 1624790: add ``syscall`` to prefix list
* bug 1619606: add ``mozilla::CheckCheckedUnsafePtrs<T>::Check`` to prefix list
* bug 1617918: fix IPC Channel Error signature generation rule
* bug 1616837: add ``RustMozCrash`` to irrelevant list
* bug 1612569: update signature generation docs
* bug 1612569: fix ``SignatureIPCChannelError`` docstring


1.0.2 (February 7th, 2020)
==========================

Bug fixes:

* bug 1612569: improve ShutDownKill signatures
* Bug 1612921 - Add some CString functions to the prefix list
* Add ``servo_arc::Arc<T>::drop_slow`` to the prefix list
* bug 1610792: add ``mozilla::DOMEventTargetHelper::AddRef`` to prefix list
* bug 1609247: move ``__security_check_cookie`` to irrelevant list
* Bug 1609247 - Add ``_security_check_cookie`` to the irrelevant signatures list
* bug 1608870: added ``mozilla::ipc::Shmem`` items to prefix list
* bug 1609121: add ``__pthread_cond_wait`` to prefix list


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
