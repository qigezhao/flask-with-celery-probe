#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

import logging
from flask import request, abort

from flask_app import app
from flask_app.manager.session.wechat import WechatMiniAppManager
from flask_app.decorator.api_response.wechat_miniapp import WechatMiniAppReponse as Response
from flask_app.decorator.performance import PerformanceProbe as Probe


@app.route('/api/session/login/wechat/miniapp')
@Probe.timeit
@Response.serialize
def api_session_wechat_login_by_miniapp():
    try:
        wx_code = request.args.get('wx_code')
        result = WechatMiniAppManager.login(wx_code)

        return result

    except Exception as e:
        abort(500)
