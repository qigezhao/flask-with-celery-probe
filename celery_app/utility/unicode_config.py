#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

import configparser as ConfigParser


class UnicodeIniParser(object):
    def __init__(self, ini_file=None, ini_string=None, *args, **kwargs):
        self.parser = ConfigParser.ConfigParser()
        if ini_string:
            self.parser.read_string(ini_string)
        elif ini_file:
            self.parser.read(ini_file, encoding='utf-8')
