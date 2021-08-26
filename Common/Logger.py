#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 21:04
# @Author  : zyc
# @File    : Logger.py
# @Software: PyCharm
import logging
import os
import time

from logging.handlers import TimedRotatingFileHandler

from Config.config import LOG_PATH,cf
cf_dict=dict(cf.data)
class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger(cf_dict.get('log').get("logger_name") if cf_dict.get('log') and cf_dict.get('log').get("logger_name") else "ROOT")
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = time.strftime("%Y-%m-%d_",time.localtime())+cf_dict.get('log').get('log_file_name') if cf_dict.get('log') and cf_dict.get('log').get('log_file_name') else 'log.log'
        self.full_log_file_name = cf_dict.get('log').get('full_log_file_name') if cf_dict.get('log') and cf_dict.get('log').get('full_log_file_name') else 'full_log.log'
        self.backup_count = int(cf_dict.get('log').get('backup_count') if cf_dict.get('log') and cf_dict.get('log').get('backup_count')  else 3)
        # 日志输出级别
        self.console_output_level = cf_dict.get('log').get('console_output_level') if cf_dict.get('log') and cf_dict.get('log').get('console_output_level') else "INFO"
        self.file_output_level = cf_dict.get('log').get('file_output_level') if cf_dict.get('log') and cf_dict.get('log').get('file_output_level') else 'DEBUG'
        self.full_output_level =cf_dict.get('log').get('full_output_level') if cf_dict.get('log') and cf_dict.get('log').get('full_output_level') else 'DEBUG'

        # 日志输出格式
        self.formatter = logging.Formatter(fmt=cf_dict.get('log').get('fommater') if cf_dict.get('log') and cf_dict.get('log').get('fommater') else 'DEBUG')

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)


            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)

            self.logger.addHandler(file_handler)
            full_handler = logging.FileHandler(
                os.path.join(LOG_PATH, self.full_log_file_name))
            full_handler.setFormatter(self.formatter)
            self.logger.addHandler(full_handler)
        return self.logger


logger = Logger().get_logger()

