# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import print_function

import argparse
import json
import sys

from .generator import SignatureGenerator


DESCRIPTION = """
Given a signature data structure as JSON via stdin, generates the signature.
"""


def main():
    """Takes crash data via stdin and generates a Socorro signature"""
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        '-v', '--verbose', help='increase output verbosity', action='store_true'
    )
    args = parser.parse_args()

    generator = SignatureGenerator(debug=args.verbose)

    crash_data = json.loads(sys.stdin.read())

    ret = generator.generate(crash_data)

    print(json.dumps(ret, indent=2))
