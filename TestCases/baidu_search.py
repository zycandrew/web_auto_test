#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 21:59
# @Author  : zyc
# @File    : baidu_search.py
# @Software: PyCharm
import unittest

from selenium import webdriver

from Common.Logger import logger
from HTMLTestRunner_Chart import HTMLTestRunner
from PageObject.baidu_page import baiduPage
class baidu_search_case(unittest.TestCase):
    """
    百度搜索用例
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls) :
        logger.info(cls.__name__)
        cls.driver.quit()
    def test_search_01(self):
        """
        百度搜索测试用例
        :return:
        """
        self.driver.get("https://www.baidu.com")
        bp=baiduPage(self.driver)
        bp.search(kw="中国")
if __name__ == '__main__':
    unittest.main()
    '''suite = unittest.TestLoader().loadTestsFromTestCase(baidu_search_case)
    runner = HTMLTestRunner(
        title="带截图，饼图，折线图，历史结果查看的测试报告",
        description="",
        stream=open("./demo.html", "wb"),
        verbosity=2,
        retry=0,
        save_last_try=True)
    runner.run(suite)'''