# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import importlib

# NOTE(willkg): We do this so that we can extract signature generation into its
# own namespace as an external library. This allows the tests to run if it's in
# "siggen" or "socorro.signature".
base_module = '.'.join(__name__.split('.')[:-2])
generator = importlib.import_module(base_module + '.generator')


class TestSignatureGenerator:
    def test_empty_dicts(self):
        generator_obj = generator.SignatureGenerator()
        ret = generator_obj.generate({})

        # NOTE(willkg): This is what the current pipeline yields. If any of those parts change, this
        # might change, too. The point of this test is that we can pass in empty dicts and the
        # SignatureGenerator and the rules in the default pipeline don't fall over.
        expected = {
            'notes': [
                'CSignatureTool: No signature could be created because we do not know '
                'which thread crashed'
            ],
            'signature': 'EMPTY: no crashing thread identified'
        }

        assert ret == expected

    def test_failing_rule(self):
        class BadRule(object):
            pass

        generator_obj = generator.SignatureGenerator(pipeline=[BadRule()])
        ret = generator_obj.generate({})

        expected = {
            'notes': [
                'Rule BadRule failed: \'BadRule\' object has no attribute \'predicate\''
            ],
            'signature': ''
        }

        assert ret == expected
