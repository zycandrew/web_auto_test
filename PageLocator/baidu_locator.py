#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 21:48
# @Author  : zyc
# @File    : baidu_locators.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

class baidu_locators(object):
    """
    百度首页元素
    """
    kw_inp=(By.XPATH,'//*[@id="kw"]')
    search_btn=(By.XPATH,'//*[@id="su"]')