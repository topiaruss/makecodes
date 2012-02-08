# Copyright 2012, Russ Ferriday
# russf@topia.com
#
#   $ easy_install qrcode
#   $ easy_install PIL
#
# and then run python makecodes.py
#
# The output files will appear in the same directory where you run the program

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
    img.save('%s.png' % title)

work = [
('http://4pps.net/1', 'Plone CMS'),
('http://4pps.net/2', 'Mayan EDMS'),
('http://4pps.net/3', 'Kotti CMS'),
('http://4pps.net/4', 'ScrumDo'),
('http://4pps.net/5', 'MediaThread'),
('http://4pps.net/6', 'KARL'),
('http://4pps.net/7', 'Askbot'),
]

[make(i, 1) for i in work]
