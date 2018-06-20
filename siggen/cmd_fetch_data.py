# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import print_function

import argparse
import json
import os
import sys

from glom import glom
import requests


class WrappedTextHelpFormatter(argparse.HelpFormatter):
    """Subclass that wraps description and epilog text taking paragraphs into account"""

    def _fill_text(self, text, width, indent):
        """Wraps text like HelpFormatter, but doesn't squash lines

        This makes it easier to do lists and paragraphs.

        """
        parts = text.split('\n\n')
        for i, part in enumerate(parts):
            # Check to see if it's a bulleted list--if so, then fill each line
            if part.startswith('* '):
                subparts = part.split('\n')
                for j, subpart in enumerate(subparts):
                    subparts[j] = super(WrappedTextHelpFormatter, self)._fill_text(
                        subpart, width, indent
                    )
                parts[i] = '\n'.join(subparts)
            else:
                parts[i] = super(WrappedTextHelpFormatter, self)._fill_text(part, width, indent)

        return '\n\n'.join(parts)


DESCRIPTION = """
Takes a crash id via the command line, pulls down the crash information, and
outputs JSON for signature generation.

To use an API token from Crash Stats to alleviate issues with rate limiting,
set SOCORRO_API_TOKEN in the environment.
"""

# FIXME(willkg): This hits production. We might want it configurable.
API_URL = 'https://crash-stats.mozilla.com/api'


def printerr(s, **kwargs):
    kwargs['file'] = sys.stderr
    print(s, **kwargs)


def fetch(endpoint, crash_id, api_token=None):
    kwargs = {
        'params': {
            'crash_id': crash_id
        }
    }
    if api_token:
        kwargs['headers'] = {
            'Auth-Token': api_token
        }

    return requests.get(API_URL + endpoint, **kwargs)


def int_or_none(data):
    if data:
        try:
            return int(data)
        except ValueError:
            printerr('int_or_none: value is not an int: %r' % data)
            return None
    return data


def cmdline():
    """Takes a crash id, pulls down data from Socorro, generates signature data"""
    parser = argparse.ArgumentParser(
        formatter_class=WrappedTextHelpFormatter,
        description=DESCRIPTION
    )
    parser.add_argument(
        '-v', '--verbose', help='increase output verbosity', action='store_true'
    )
    parser.add_argument(
        'crashid', help='crash id to generate signatures for'
    )

    args = parser.parse_args()

    api_token = os.environ.get('SOCORRO_API_TOKEN', '')

    crash_id = args.crashid.strip()

    resp = fetch('/RawCrash/', crash_id, api_token)
    if resp.status_code == 404:
        printerr('%s: does not exist.' % crash_id)
        return 1
    if resp.status_code == 429:
        printerr('API rate limit reached. %s' % resp.content)
        # FIXME(willkg): Maybe there's something better we could do here. Like maybe wait a
        # few minutes.
        return 1
    if resp.status_code == 500:
        printerr('HTTP 500: %s' % resp.content)
        return 1

    raw_crash = resp.json()

    # If there's an error in the raw crash, then something is wrong--probably with the API
    # token. So print that out and exit.
    if 'error' in raw_crash:
        print('Error fetching raw crash: %s' % raw_crash['error'], file=sys.stderr)
        return 1

    resp = fetch('/ProcessedCrash/', crash_id, api_token)
    if resp.status_code == 404:
        printerr('%s: does not have processed crash.' % crash_id)
        return 1
    if resp.status_code == 429:
        printerr('API rate limit reached. %s' % resp.content)
        # FIXME(willkg): Maybe there's something better we could do here. Like maybe wait a
        # few minutes.
        return 1
    if resp.status_code == 500:
        printerr('HTTP 500: %s' % resp.content)
        return 1

    processed_crash = resp.json()

    # If there's an error in the processed crash, then something is wrong--probably with the
    # API token. So print that out and exit.
    if 'error' in processed_crash:
        printerr('Error fetching processed crash: %s' % processed_crash['error'])
        return 1

    # We want to generate fresh signatures, so we remove the "normalized" field
    # from stack frames from the processed crash because this is essentially
    # cached data from previous processing
    for thread in processed_crash['json_dump'].get('threads', []):
        for frame in thread.get('frames', []):
            if 'normalized' in frame:
                del frame['normalized']

    crash_data = {
        # JavaStackTrace or None
        'java_stack_trace': glom(raw_crash, 'JavaStackTrace', default=None),

        # int or None
        'crashing_thread': glom(
            processed_crash, 'json_dump.crash_info.crashing_thread', default=0
        ),

        # list of CStackTrace or None
        'threads': glom(processed_crash, 'json_dump.threads', default=None),

        # int or None
        'hang_type': glom(processed_crash, 'hang_type', default=None),

        # text or None
        'os': glom(processed_crash, 'json_dump.system_info.os', default=None),

        # int or None
        'oom_allocation_size': int_or_none(glom(raw_crash, 'OOMAllocationSize', default=None)),

        # text or None
        'abort_message': glom(raw_crash, 'AbortMessage', default=None),

        # text or None
        'mdsw_status_string': glom(processed_crash, 'mdsw_status_string', default=None),

        # text json with "phase", "conditions" (complicated--see code) or None
        'async_shutdown_timeout': glom(raw_crash, 'AsyncShutdownTimeout', default=None),

        # text or None
        'jit_category': glom(processed_crash, 'classifications.jit.category', default=None),

        # text or None
        'ipc_channel_error': glom(raw_crash, 'ipc_channel_error', default=None),

        # text or None
        'ipc_message_name': glom(raw_crash, 'IPCMessageName', default=None),

        # text
        'moz_crash_reason': glom(raw_crash, 'MozCrashReason', default=None),

        # list of text; e.g. ["browser"]
        'additional_minidumps': glom(raw_crash, 'additional_minisumps', default=[]),
    }

    print(json.dumps(crash_data, indent=2))
