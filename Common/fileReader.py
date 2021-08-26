#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 20:00
# @Author  : zyc
# @File    : fileReader.py
# @Software: PyCharm
import configparser
import os
import yaml
from xlrd import open_workbook



class yamlReader:
    """
    读取yaml类型的配置文件
    """
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf=yamlf
        else:
            raise FileNotFoundError(f"{yamlf}文件不存在")
        self._data=None
    @property
    def data(self):
        """只读属性data"""
        #第一次打开yamlf 加载data，否则直接读取之前保存的data
        if not self._data:
            with open(self.yamlf,'rb',encoding='utf8') as f:
                #list_all生成一个generator ，用list生成列表类型
                self.__data=list(yaml.load_all(f))
        return self._data

class SheetTypeError(Exception):
    pass

class excelReader:
    """读取excel文件"""
    def __init__(self,excelf,sheet=0,title_line=True):


        if os.path.exists(excelf):
            self.excelf = excelf

        else:
             raise FileNotFoundError(f"{excelf}文件不存在！")

        self.sheet = sheet
        self.title_line = title_line
        self._data = list()
    @property
    def data(self):
        if not self._data:
            workbook=open_workbook(self.excelf)
            if type(self.sheet) not in [int,str]:
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)
            if self.title_line:
                title = s.row_values(0)  # 首行为title
                for col in range(1, s.nrows):
                    # 依次遍历其余行，与首行组成dict，拼到self._data中
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    # 遍历所有行，拼到self._data中
                    self._data.append(s.row_values(col))
            return self._data
class iniReader:
    """读取 *.ini 类型的配置文件"""
    def __init__(self,inif,datatype=''):
        if os.path.exists(inif):
            self.inif=inif
        else:
            raise FileNotFoundError(f"{inif} 文件不存在")
        self._data=None
        self.datatype=datatype.lower()

    @property
    def data(self):
        if not self._data:
            config = configparser.ConfigParser()
            config.read(self.inif,encoding="utf-8")

            if self.datatype=='dict':
                return config._sections
            else:
                return  config