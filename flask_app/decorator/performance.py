#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

import logging

import time
import functools

from celery_app.task_probe import task_performance_probe_save


class TimeitProbe(object):
    def __init__(self, name):
        self.name = name
        self.time_begin = time.time()
        self.time_end = self.time_begin
        self.elapsed = self.time_end - self.time_begin

    @property
    def payload(self):
        return dict(
            topic=self.name,
            value=self.elapsed,
            recorded_at=self.time_end,
            expired_at=self.time_end + 300,
        )

    def done(self):
        self.time_end = time.time()
        self.elapsed = self.time_end - self.time_begin


class PerformanceProbe(object):
    @staticmethod
    def async_save_probe(probe):
        payload = probe.payload
        logging.debug('PerformanceProbe.async_save_probe(payload={})'.format(payload))
        task_performance_probe_save.delay(payload)

    @staticmethod
    def timeit(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            probe = TimeitProbe(func.__name__)
            data = func(*args, **kwargs)

            probe.done()
            PerformanceProbe.async_save_probe(probe)

            return data

        return wrapper
