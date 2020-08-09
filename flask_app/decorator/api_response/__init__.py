#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

import json
import functools


class GenericJsonResponse(object):
    @staticmethod
    def is_validate(data):
        if isinstance(data, list):
            return 1
        elif isinstance(data, dict):
            return 1
        else:
            return 0 if data else -1

    @staticmethod
    def format(data):
        response = dict(
            errno=GenericJsonResponse.is_validate(data),
            data=data,
        )
        return json.dumps(response, separators=(',', ':'), ensure_ascii=False)

    @staticmethod
    def serialize(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            return GenericJsonResponse.format(data)

        return wrapper
