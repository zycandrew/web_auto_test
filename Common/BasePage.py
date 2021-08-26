#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 20:43
# @Author  : zyc
# @File    : BasePage.py
# @Software: PyCharm
from Common.Logger import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import datetime

class pageError(Exception):
    pass

class BasePage(object):
    """
    selenium二次封装
    1、封装基本函数、执行日志、异常处理、失败截图
    2、页面公有功能，业务无关
    """
    def __init__(self,driver):
        self.driver=driver
    def wait_element_visible(self,locator,times=3,poll_frequency=0.5,doc=""):
        """
        显性等待元素
        :param locator: 元素定位元组（定位类型，定位方式）
        :param times:最大等待时间
        :param poll_frequency:等待周期
        :param doc:注释 模块——界面——操作
        :return:返回定位的元素
        """
        logger.info(f"等待元素{locator}元素可见")
        try:
            #开始等待时间
            time_start=datetime.datetime.now()
            ele=WebDriverWait(self.driver,times,poll_frequency).until(EC.visibility_of_element_located(locator))
            #结束时间
            time_end=datetime.datetime.now();
            #等待时间
            time_wait=(time_end-time_start).seconds
            logger.info(f"{doc}:元素{locator}可见，等待结束，等待开始时间：{time_start},等待结束时间：{time_end},等待时长：{time_wait}")
            return ele
        except Exception as e:
            #30秒内定位不到元素，捕捉异常写进日志
            logger.error(f"{doc}:元素{locator}等待可见失败",exc_info=True)
    def get_element(self,locator,doc=""):
        """
        查找元素
        :param locator: 元素定位元组
        :return: 返回元素
        """
        logger.info(f"{doc}:查找{locator}元素")
        try:
            ele=self.wait_element_visible(locator,doc=doc)
            return ele
        except:
            logger.error(f"{doc}:{locator}元素查找失败",exc_info=True)

    def click_element(self,locator,doc=""):
        """
        单击事件
        :param locator:
        :return:
        """
        ele=self.get_element(locator,doc=doc)

        logger.info(f"{doc}:点击{locator}元素")
        try:
            ele.click()
        except Exception:
            logger.error(f"{doc}:{locator}元素点击失败！",exc_info=True)

    def input_text(self,locator,text,doc=""):
        """
        输入文本
        :param text: 输入内容
        :return:
        """
        ele=self.get_element(locator,doc=doc)
        logger.info(f"{doc}:{locator}元素输入内容：{text}")
        try:
            ele.send_keys(text)
        except:
            logger.error(f"{doc}:{locator}元素输入 {text} 操作失败",exc_info=True)
    def get_text(self,locator,doc=""):
        """
        获得元素文本
        :param locator:
        :param doc:
        :return:
        """
        ele=self.get_element(locator,doc=doc)
        logger.info(f"{doc}:获取{locator}元素文本内容")
        try:
            ele.text
        except:
            logger.error(f"{doc}:获取{locator}元素文本内容失败！",exc_info=True)

