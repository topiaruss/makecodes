# Copyright 2012, Russ Ferriday
# russf@topia.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import qrcode


def make(job, fit=False, box=10):
    url, title = job

    qr = qrcode.QRCode(
      version=fit and 1 or None,
      error_correction=qrcode.constants.ERROR_CORRECT_H,
      box_size=box,
    )
    qr.add_data(url)
    img = qr.make_image()
    img.save('%s.pdf' % title)

work = [
    ('http://4pps.net/q/1', 'Plone CMS'),
    ('http://4pps.net/q/2', 'Mayan EDMS'),
    ('http://4pps.net/q/3', 'Kotti CMS'),
    ('http://4pps.net/q/4', 'ScrumDo'),
    ('http://4pps.net/q/5', 'MediaThread'),

    # not sure about these, yet...
    ('http://4pps.net/q/6', 'KARL'),
    ('http://4pps.net/q/7', 'Askbot'),
    ('http://4pps.net/q/8', 'Mezzanine'),
    ('http://4pps.net/q/9', 'Miro Community'),
    ('http://4pps.net/q/0', 'Django CMS'),

    # and these are for category comparisons
    ('http://4pps.net/q/A', 'CMS'),  # Must include Plone, Kotti, DjCMS, if we use it
    ('http://4pps.net/q/B', 'EDMS'),  # Can include Mayan and maybe Plone??
    ('http://4pps.net/q/C', 'DevTools'),  # Can include ScrumDo
    ('http://4pps.net/q/D', 'Media'),  # Can include MediaThread, Mayan, MiroC if used.
    ]

[make(i, 1) for i in work]
