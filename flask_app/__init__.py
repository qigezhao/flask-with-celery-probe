#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

from flask import Flask

app = Flask(
    __name__,
)

# login via wechat miniapp (wx_code)
from flask_app.api_session_wechat import api_session_wechat_login_by_miniapp

# user profile
from flask_app.api_profile import api_session_profile_find
