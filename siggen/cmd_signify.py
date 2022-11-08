# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import print_function

import argparse
import json
import sys

from .generator import SignatureGenerator
from .utils import convert_to_crash_data


DESCRIPTION = """
Given a signature data structure as JSON via stdin, generates the signature.

If you pass a processed crash, this will convert it.
"""


def main():
    """Takes crash data via stdin and generates a Socorro signature"""
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_true"
    )
    parser.add_argument(
        "--signature-list-dir",
        required=False,
        help=(
            "directory of signature list files to use; if not specified, uses the "
            + "included signature list files"
        ),
    )
    args = parser.parse_args()

    generator_kwargs = {}
    if args.signature_list_dir:
        generator_kwargs = {
            "signature_list_dir": args.signature_list_dir,
        }
    generator = SignatureGenerator(**generator_kwargs)

    crash_data = json.loads(sys.stdin.read())

    if "json_dump" in crash_data:
        # This is an indicator that the crash data is a processed crash and
        # needs to be converted
        if args.verbose:
            print("Crash data is a processed crash. Converting ...")
        crash_data = convert_to_crash_data(crash_data)

    result = generator.generate(crash_data)
    if args.verbose:
        for item in result.debug_log:
            print(item)

    return_dict = {
        "signature": result.signature,
        "proto_signature": result.extra.get("proto_signature", ""),
        "notes": result.notes,
    }
    print(json.dumps(return_dict, indent=2))
