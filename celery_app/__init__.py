#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

import logging
from celery import Celery
from celery_app.config import Config

cfg = Config.get_instance()
app_config = dict(broker=cfg.celery_broker, backend=cfg.celery_backend)

app = Celery(__name__, **app_config)
app.config_from_object('celery_app.celery_config')
