#!/bin/bash

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Runs commands and spits out help text.

# Usage: bin/run_cmd_tests.sh [--non-zero-exit]

set -e

signify --help

if [[ "$1" == "--no-requests" ]]; then
    fetch-data --help && /bin/false || /bin/true
    signature --help && /bin/false || /bin/true

else
    fetch-data --help
    signature --help
fi
