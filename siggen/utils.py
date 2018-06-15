# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


def drop_unicode(text):
    """Takes a text and drops all unicode characters

    :arg str/unicode text: the text to fix

    :returns: text with all unicode characters dropped

    """
    if isinstance(text, str):
        # Convert any str to a unicode so that we can convert it back and drop any non-ascii
        # characters
        text = text.decode('unicode_escape')

    return text.encode('ascii', 'ignore')
