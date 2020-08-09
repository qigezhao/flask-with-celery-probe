#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

import logging

import threading

from celery_app.utility.unicode_config import UnicodeIniParser

# predefine
CELERY_CONFIG_FILE = '/etc/celery-app.conf'


class Config(UnicodeIniParser):
    instance_lock = threading.Lock()

    def __init__(self, from_file=CELERY_CONFIG_FILE, from_string=None, *args, **kwargs):
        super().__init__(from_file, from_string)

    # ISingleton
    @classmethod
    def get_instance(cls, *args, **kwargs):
        with cls.instance_lock:
            if not hasattr(cls, "instance"):
                cls.instance = cls(*args, **kwargs)

        return cls.instance

    def __getattr__(self, item, section='default', value_default=''):
        if item in self.__dict__:
            return self.__dict__[item]

        if section in self.parser.sections():
            return self.parser.get(section, item)
        return value_default
