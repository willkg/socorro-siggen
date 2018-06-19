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
    crash_data = {}

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

    crash_data.update({
        'JavaStackTrace': raw_crash.get('JavaStackTrace', None),
        'OOMAllocationSize': raw_crash.get('OOMAllocationSize', None),
        'AbortMessage': raw_crash.get('AbortMessage', None),
        'AsyncShutdownTimeout': raw_crash.get('AsyncShutdownTimeout', None),
        'ipc_channel_error': raw_crash.get('ipc_channel_error', None),
        'additional_minidumps': raw_crash.get('additional_minidumps', None),
        'IPCMessageName': raw_crash.get('IPCMessageName', None),
        'MozCrashReason': raw_crash.get('MozCrashReason', None),
    })

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

    crash_data.update({
        'hang_type': processed_crash.get('hang_type', None),
        'json_dump': {
            'threads': glom(processed_crash, 'json_dump.threads', default=[]),
            'system_info': {
                'os': glom(processed_crash, 'json_dump.system_info.os', default=''),
            },
            'crash_info': {
                'crashing_thread': glom(
                    processed_crash, 'json_dump.crash_info.crashing_thread', default=None
                ),
            },
        },
        'mdsw_status_string': processed_crash.get('mdsw_status_string', None),
    })

    # We want to generate fresh signatures, so we remove the "normalized" field from stack
    # frames because this is essentially cached data from processing
    for thread in crash_data['json_dump'].get('threads', []):
        for frame in thread.get('frames', []):
            if 'normalized' in frame:
                del frame['normalized']

    print(json.dumps(crash_data, indent=2))
