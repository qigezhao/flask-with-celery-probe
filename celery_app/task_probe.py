#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

import logging
from celery_app import app


@app.task(bind=True)
def task_performance_probe_save(self, payload, *args, **kwargs):
    result = dict(result='failed')
    try:
        result.update(dict(result='success', payload=payload, ))

    except Exception as e:
        component = 'celery_app.task_probe.celery_task_performance_probe_save'
        logging.error('{}(args={}, kwargs={})'.format(component, args, kwargs))

    finally:
        return result
