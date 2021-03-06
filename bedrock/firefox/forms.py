# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

from django import forms

from lib.l10n_utils.dotlang import _

LANG_FILES = ['firefox/whatsnew-fx37']


class SMSSendForm(forms.Form):
    number = forms.CharField(max_length=14)
    optin = forms.BooleanField(required=False)

    def clean_number(self):
        mobile = self.cleaned_data['number']
        mobile = re.sub(r'\D+', '', mobile)
        if len(mobile) == 10:
            mobile = '1' + mobile
        elif len(mobile) != 11 or mobile[0] != '1':
            raise forms.ValidationError(_(
                'Sorry. This number isn\'t valid. Please enter a U.S. phone '
                'number or <a href="%s">'
                'download directly from Google Play.</a>'
            ) % ('http://mzl.la/OgZo6k'))
        return mobile
