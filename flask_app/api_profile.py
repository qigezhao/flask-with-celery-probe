#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

import logging
from flask import request, abort

from flask_app import app


@app.route('/api/session/profile/find')
def api_session_profile_find():
    try:
        token = request.args.get('token')
        return token

    except Exception as e:
        abort(500)
