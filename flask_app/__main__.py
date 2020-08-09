#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

from optparse import OptionParser
from flask_app import app

option = OptionParser()
option.add_option('-p', '--port', dest='port', default=8800)
option.add_option('--debug', dest='is_debug', action='store_true', default=False)
(user, args) = option.parse_args()

app.run(
    port=user.port,
    debug=user.is_debug,
)
