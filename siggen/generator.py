# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging

from siggen.rules import (
    SignatureGenerationRule,
    StackwalkerErrorSignatureRule,
    OOMSignature,
    AbortSignature,
    SignatureShutdownTimeout,
    SignatureRunWatchDog,
    SignatureIPCChannelError,
    SignatureIPCMessageName,
    SigFixWhitespace,
    SigTruncate,
    SignatureJitCategory,
    SignatureParentIDNotEqualsChildID,
)


DEFAULT_PIPELINE = [
    SignatureGenerationRule(),
    StackwalkerErrorSignatureRule(),
    OOMSignature(),
    AbortSignature(),
    SignatureShutdownTimeout(),
    SignatureRunWatchDog(),
    SignatureIPCChannelError(),
    SignatureIPCMessageName(),
    SignatureParentIDNotEqualsChildID(),
    SignatureJitCategory(),

    # NOTE(willkg): These should always come last and in this order
    SigFixWhitespace(),
    SigTruncate(),
]


logger = logging.getLogger(__name__)


class SignatureGenerator:
    def __init__(self, pipeline=None, debug=False):
        self.pipeline = pipeline or list(DEFAULT_PIPELINE)
        self.debug = debug

    def generate(self, signature_data):
        """Takes data and returns a signature

        :arg dict signature_data: data to use to generate a signature

        :returns: dict containing ``signature`` and ``notes`` keys representing the
            signature and processor notes

        """
        # NOTE(willkg): Rules mutate the result structure in-place
        result = {
            'signature': '',
            'notes': []
        }

        for rule in self.pipeline:
            try:
                if rule.predicate(signature_data, result):
                    old_sig = result['signature']
                    rule.action(signature_data, result)

                    if self.debug:
                        result['notes'].append(
                            '%s: %s -> %s' % (
                                rule.__class__.__name__,
                                old_sig,
                                result['signature']
                            )
                        )

            except Exception as exc:
                logger.exception('Error running %r', rule)
                result['notes'].append('Rule %s failed: %s' % (rule.__class__.__name__, exc))

        return result
