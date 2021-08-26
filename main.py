#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 20:43
# @Author  : zyc
# @File    : main.py
# @Software: PyCharm
import requests

from requests_toolbelt.utils import dump
from Common.email import Email




""""url = "http://httpbin.org/post"
data = {"name": "hanzhichao", "age": 18} # Post请求发送的数据，字典格式
headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
res = requests.post(url=url, data=data, headers=headers) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数

data = dump.dump_all(res)
print(data.decode('utf-8'))"""

email=Email('smtp.qq.com','643069710@qq.com','uvihmmvblbtrbfib','zyc_tiger@163.com','test',message="123456789")
print(email.msg)
email.send()



