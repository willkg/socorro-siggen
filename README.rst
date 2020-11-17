==============
socorro-siggen
==============

This is an extraction of the Socorro crash signature generation code.

:Code: https://github.com/willkg/socorro-siggen
:Documentation: Check the ``README.rst`` file
:Changelog: Check the ``HISTORY.rst`` file
:Issue tracker: https://github.com/willkg/socorro-siggen/issues
:License: MPLv2
:Status: Stable
:Community Participation Guidelines: `<https://github.com/willkg/socorro-siggen/blob/main/CODE_OF_CONDUCT.md>`_


Installing
==========

socorro-siggen is available on `PyPI <https://pypi.org/project/siggen/>`_. You
can install it with::

    $ pip install siggen


Basic use
=========

Use it on the command line for signature generation debugging
-------------------------------------------------------------

You can generate a JSON output of the signature result from the command line::

    $ cat <JSONFILE> | signify
    SIGNATURE HERE

You can pass in a ``--verbose`` flag and get verbose output about how the
signature was generated.

You can generate a JSONFILE to pass into signify using crash ids from Crash
Stats::

    $ fetch-data CRASHID > crash.json

You can fetch crash data from Crash Stats, generate a signature, and get some
output as to whether it matches the signature for that crash report in Crash
Stats::

    $ signature CRASHID

This helps when adjusting siglist and fixing signature generation problems.


Use it as a library
-------------------

You can use socorro-siggen as a library::

    from siggen.generator import SignatureGenerator

    generator = SignatureGenerator()

    crash_data = {
        ...
    }

    ret = generator.generate(crash_data)
    print(ret['signature'])


Things to know
==============

Things to know about siggen:

1. Make sure to use the latest version of siggen and update frequently.
   We use semantic versioning, so the API will not change for MINOR
   and PATCH releases. Feel free to restrict on the MAJOR version.

2. Signatures generated will change between siggen versions. The API
   may be stable, but bug fixes and changes to the siglist files will
   affect signature generation output. Hopefully for the better!

3. If you have problems, please open up an issue. Please include the
   version of siggen.

   When using siggen, you can find the version like this::

       import siggen
       print(siggen.__version__)


Crash data schema
=================

This is the schema for the crash data structure::

  {
    crashing_thread: <int or null>,    // Optional, The index of the crashing thread in threads.
                                       // This defaults to None which indicates there was no
                                       // crashing thread identified in the crash report.

    threads: [                         // Optional, list of stack traces for c/c++/rust code.
      {
        frames: [                      // List of one or more frames.
          {
            function: <string>,        // Optional, The name of the function.
                                       // If this is ``None`` or not in the frame, then signature
                                       // generation will calculate something using other data in
                                       // the frame.

            module: <string>,          // Optional, name of the module
            file: <string>,            // Optional, name of the file
            line: <int>,               // Optional, line in the file
            module_offset: <string>,   // Optional, offset in hex in the module for this frame
            offset: <string>           // Optional, offset in hex for this frame

                                       // Signature parts are computed using frame data in this
                                       // order:

                                       // 1. if there's a function (and optionally line)--use
                                       //    that
                                       // 2. if there's a file and a line--use that
                                       // 3. if there's an offset and no module/module_offset--use
                                       //    that
                                       // 4. use module/module_offset
          }
          // ... additional frames
        ],

        thread_name: <string>,         // Optional, The name of the thread.
                                       // This isn't used, yet, but might be in the future for
                                       // debugging purposes.

        frame_count: <int>             // Optional, This is the total number of frames. This
                                       // isn't used.
      },
      // ... additional threads
    ],

    java_stack_trace: <string>,        // Optional, If the crash is a Java crash, then this will
                                       // be the Java traceback as a single string. Signature
                                       // generation will split this string into lines and then
                                       // extract frame information from it to generate the
                                       // signature.

                                       // FIXME(willkg): Write up better description of this.

    oom_allocation_size: <int>,        // Optional, The allocation size that triggered an
                                       // out-of-memory error. This will get added to the
                                       // signature if one of the indicator functions appears in
                                       // the stack of the crashing thread.

    abort_message: <string>,           // Optional, The abort message for the crash, if there is
                                       // one. This is added to the beginning of the signature.

    hang_type: <int>,                  // Optional.
                                       // 1 here indicates this is a chrome hang and we look at
                                       // thread 0 for generation.
                                       // -1 indicates another kind of hang.

    async_shutdown_timeout: <text>,    // Optional, This is a text field encoded in JSON with
                                       // "phase" and "conditions" keys.
                                       // FIXME(willkg): Document this structure better.

    jit_category: <string>,            // Optional, If there's a JIT classification in the
                                       // crash, then that will override the signature

    ipc_channel_error: <string>,       // Optional, If there is an IPC channel error, it
                                       // replaces the signature.

    ipc_message_name: <string>,        // Optional, This gets added to the signature if there
                                       // was an IPC message name in the crash.

    additional_minidumps: <string>,    // Optional, A crash report can contain multiple minidumps.
                                       // This is a comma-delimited list of minidumps other than
                                       // the main one that the crash had.

                                       // Example: "browser,flash1,flash2,content"

    mdsw_status_string: <string>,      // Optional, Socorro-generated
                                       // This is the minidump-stackwalk status string. This
                                       // gets generated when the Socorro processor runs the
                                       // minidump through minidump-stackwalk. If you're not
                                       // using minidump-stackwalk, you can ignore this.

    moz_crash_reason: <string>,        // Optional, This is the MOZ_CRASH_REASON value. This
                                       // doesn't affect anything unless the value is
                                       // "MOZ_RELEASE_ASSERT(parentBuildID == childBuildID)".

    os: <string>,                      // Optional, The name of the operating system. This
                                       // doesn't affect anything unless the name is "Windows
                                       // NT" in which case it will lowercase module names when
                                       // iterating through frames to build the signature.
  }


Missing keys in the structure are treated as ``None``, so you can pass in a
minimal structure with just the parts you define.


Examples
========

Example almost minimal, somewhat nonsense ``crash_data.json``::

    {
        "os": "Linux",
        "crashing_thread": 0,
        "threads": [
            {
                "frames": [
                    {
                        "frame": 0,
                        "function": "SomeFunc",
                        "line": 20,
                        "file": "somefile.cpp",
                        "module": "foo.so.5.15.0",
                        "module_offset": "0x37a92",
                        "offset": "0x7fc641052a92"
                    },
                    {
                        "frame": 1,
                        "function": "SomeOtherFunc",
                        "line": 444,
                        "file": "someotherfile.cpp",
                        "module": "bar.so",
                        "module_offset": "0x39a55",
                        "offset": "0x7fc641044a55"
                    }
                ]
            }
        ]
    }


That produces this output::

    $ cat crash_data.json | signify
    {
      "notes": [],
      "proto_signature": "SomeFunc | SomeOtherFunc",
      "signature": "SomeFunc"
    }


Release process
===============

1. Create branch
2. Update version and release date in ``siggen/__init__.py``
3. Update ``HISTORY.rst``
4. Push the branch, create a PR, review it, merge it
5. Create a signed tag, push to github::

     git tag -s v0.1.0
     git push --tags REMOTE TAGNAME

6. Build::

     python setup.py sdist bdist_wheel

   Make sure to use Python 3 with an updated ``requirements-dev.txt``.

7. Upload to PyPI::

     twine upload dist/*
