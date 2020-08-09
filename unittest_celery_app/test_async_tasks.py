#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

import unittest

from celery_app.task_probe import task_performance_probe_save


class TestAsyncTasks(unittest.TestCase):

    def test_async_save_probe(self):
        payload = {
            "topic": "api_session_wechat_login_by_miniapp",
            "value": 0.00027680397033691406,
            "recorded_at": 1596952989.2517388,
            "expired_at": 1596953289.2517388,
        }

        task = task_performance_probe_save.delay(payload)
        self.assertTrue(task, 'test_async_save_probe() failed')

        result = task.get(timeout=10)
        self.assertIsInstance(result, dict, 'result is not dict')
        self.assertTrue('result' in result, 'result has no key named result')
