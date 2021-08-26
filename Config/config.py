#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 19:36
# @Author  : zyc
# @File    : config.py
# @Software: PyCharm
import os
from Common import fileReader

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.ini')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'OutPut','logs')
REPORT_PATH = os.path.join(BASE_PATH,'OutPut', 'reports')
cf=fileReader.iniReader(CONFIG_FILE,datatype='dict')

