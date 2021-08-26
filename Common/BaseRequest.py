#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 20:02
# @Author  : zyc
# @File    : BaseRequest.py
# @Software: PyCharm
import requests
from Common.Logger import logger


class UnSupportMethodException(Exception):
    """当传入的method的参数不是支持的类型时抛出此异常。"""
    pass

METHOD_TYPES=['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']
class BaseRequest(object):
    """request 接口请求基类"""
    def __init__(self, url, method='GET', headers=None, cookies=None):
        """

        :param url: 访问地址
        :param method: 请求方式
        :param headers: 请求头 {}
        :param cookies: cookies {}
        """
        self.url=url
        self.session=requests.session()
        self.method=method.upper()
        if(self.method not in METHOD_TYPES):
            raise UnSupportMethodException("无效请求方式{0}".format(self.method))
        self.set_headers(headers)
        self.set_cookies(cookies)
    def set_headers(self,headers):
        """设置请求头"""
        if headers:

            self.session.headers.update(headers)
    def set_cookies(self,cookies):
        """设置请求头"""
        if cookies:
            self.session.cookies.update(cookies)

    def send(self, params=None, data=None, **kwargs):
        """

        :param params: url参数
        :param data: 请求数据
        :param kwargs:
        :return: response
        """
        try:
            response = self.session.request(method=self.method, url=self.url, params=params, data=data, **kwargs)
            response.encoding = 'utf-8'
            logger.info('{0} | {1}'.format(self.method, self.url))
            logger.info('headers:\n {0}'.format(response.headers))
            logger.info('请求成功: {0}\n{1}'.format(response, response.text))
        except:
            logger.error("请求异常：",exc_info=True)
        return response
