#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import configparser
from config import base_dir

config_path = base_dir.INI_PATH


class ReadConfig:
    """配置文件"""

    def __init__(self):
        if not os.path.exists(config_path):
            raise FileNotFoundError("配置文件%s不存在！" % config_path)
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(config_path, encoding='utf-8')




    def get_value(self,section,option):
        """获取"""
        return self.config.get(section, option)


if __name__ == '__main__':
   pass

