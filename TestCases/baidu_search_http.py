#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 20:32
# @Author  : zyc
# @File    : baidu_search_http.py
# @Software: PyCharm
import unittest

from Common.BaseRequest import BaseRequest


class baidu_search_http(unittest.TestCase):

    def test_get_baidu(self):
        url="https://www.baidu.com/"
        brq=BaseRequest(url)
        brq.send()


