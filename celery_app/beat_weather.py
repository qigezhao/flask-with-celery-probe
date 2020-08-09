#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

import logging
from celery_app import app


@app.task(bind=True)
def beat_fetch_weather(self, *args, **kwargs):
    result = dict(result='failed')
    try:
        result.update(dict(result='success'))

    except Exception as e:
        component = 'celery_app.beat_weather.celery_beat_fetch_weather'
        logging.error('{}(args={}, kwargs={})'.format(component, args, kwargs))

    finally:
        return result
