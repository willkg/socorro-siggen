==============
socorro-siggen
==============

This is an experimental extraction of the Socorro signature generation code.

:Code:          https://github.com/willkg/socorro-siggen
:Documentation: Check the ``README.rst`` file
:Changelog:     Check the ``HISTORY.rst`` file
:Issue tracker: https://github.com/willkg/socorro-siggen/issues
:License:       MPLv2
:Status:        Alpha


Installing
==========

socorro-siggen is available on `PyPI <https://pypi.org>`_. You can install it
with::

    $ pip install siggen


Basic use
=========

You can use socorro-siggen as a command line::

    $ signify <JSONFILE>
    SIGNATURE HERE


Alternatively::

    $ cat <JSONFILE> | signify


You can use socorro-siggen as a library::

    from siggen import SignatureGenerator

    generator = SignatureGenerator()

    crash_data = {
        ...
    }

    ret = generator.generate(crash_data)
    print(ret['signature'])


Crash data schema
=================

This is the schema for the crash data structure: ::

    {
      "type": "object",
      "$schema": "http://json-schema.org/schema#",
      "properties": {
        "crashing_thread": {
          "type": "integer",
          "description": "The index of the crashing thread in threads.",
          "default": 0
        },
        "threads": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "frames": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "function": {
                      "type": "string",
                      "description": "The name of the function. If this is `None` or not in the frame, then signature generation will calculate something using other data in the frame."
                    },
                    "module": {
                      "type": "string",
                      "description": "The name of the module.",
                      "required": true
                    },
                    "file": {
                      "type": "string",
                      "description": "The name of the file.",
                      "required": true
                    },
                    "line": {
                      "type": "integer",
                      "description": "The line in the file.",
                      "required": true
                    },
                    "module_offset": {
                      "type": "string",
                      "description": "The offset in hex in the module for this frame.",
                      "required": true
                    },
                    "offset": {
                      "type": "string",
                      "description": "The offset in hex for this frame.",
                      "required": true
                    }
                  }
                }
              },
              "thread_name": {
                "type": "string",
                "description": "The name of the thread. This isn't used, yet, but might be in the future for debugging purposes."
              },
              "frame_count": {
                "type": "integer",
                "description": "This is the total number of frames. This isn't used."
              }
            }
          }
        },
        "java_stack_trace": {
          "type": "string",
          "description": "If the crash is a Java crash, then this will be the Java traceback as a single string. Signature generation will split this string into lines and then extract frame information from it to generate the signature.",
          "FIXME(willkg)": "Write up better description of this."
        },
        "oom_allocation_size": {
          "type": "integer",
          "description": "The allocation size that triggered an out-of-memory error. This will get added to the signature if one of the indicator functions appears in the stack of the crashing thread."
        },
        "abort_message": {
          "type": "string",
          "description": "The abort message for the crash, if there is one. This is added to the beginning of the signature."
        },
        "hang_type": {
          "type": "integer",
          "description": " A value of 1 here indicates this is a chrome hang and we look at thread 0 for generation. A value of -1 indicates another kind of hang. All other values indicate this crash is not a hang at all."
        },
        "async_shutdown_timeout": {
          "type": "string",
          "description": "This is a text field encoded in JSON with 'phase' and 'conditions' keys."
        },
        "jit_category": {
          "type": "string",
          "description": "If there's a JIT classification in the crash, then that will override the signature."
        },
        "ipc_channel_error": {
          "type": "string",
          "description": "If there is an IPC channel error, it replaces the signature."
        },
        "ipc_message_name": {
          "type": "string",
          "description": "This gets added to the signature if there was an IPC message name in the crash."
        },
        "additional_minidumps": {
          "type": "array",
          "description": "A crash report can contain multiple minidumps. This is the list of minidumps other than the main one that the crash had.",
          "items": {
            "type": "string"
          }
        },
        "mdsw_status_string": {
          "type": "string",
          "description": "This is the minidump-stackwalk status string. This gets generated when the Socorro processor runs the minidump through minidump-stackwalk. If you're not using minidump-stackwalk, you can ignore this."
        },
        "moz_crash_reason": {
          "type": "string",
          "description": "This is the MOZ_CRASH_REASON value. This doesn't affect anything unless the value is 'MOZ_RELEASE_ASSERT(parentBuildID == childBuildID)'."
        },
        "os": {
          "type": "string",
          "description": "The name of the operating system. This doesn't affect anything unless the name is 'Windows NT' in which case it will lowercase module names when iterating through frames to build the signature."
        }
      }
    }

Signature parts are computed using frame data in this order:

    1. if there's a function (and optionally line)--use that
    2. if there's a file and a line--use that
    3. if there's an offset and no module/module_offset--use that
    4. use module/module_offset

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
     git push --tags [REMOTE] master

6. Build::

     python setup.py sdist bdist_wheel

7. Upload to PyPI::

     twine upload dist/*
