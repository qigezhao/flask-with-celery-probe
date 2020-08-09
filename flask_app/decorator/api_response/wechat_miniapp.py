#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

import json
import functools


class WechatMiniAppReponse(object):
    @staticmethod
    def serialize(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            return json.dumps(data, ensure_ascii=False)

        return wrapper
