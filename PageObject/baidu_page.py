#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 21:44
# @Author  : zyc
# @File    : baidu_page.py
# @Software: PyCharm
from Common.BasePage import BasePage
from PageLocator.baidu_locator import baidu_locators as loc

class baiduPage(BasePage):
    """
    百度首页
    """
    def search(self,kw):
        """

        :param kw: 搜索词条
        :return:
        """
        doc="百度首页——搜索"
        #kw_input=self.get_element(loc.kw_inp,doc=doc)
        self.input_text(loc.kw_inp,kw,doc=doc)
        self.click_element(loc.search_btn,doc=doc)