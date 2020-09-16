#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml
from config.base_dir import ELEMENT_PATH
class GetYaml:
    """获取元素"""

    def __init__(self, name):
        self.file_name = '%s.yml' % name
        self.element_path = os.path.join(ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)#将yaml转换python


    def __getitem__(self, item):#实例对象的key不管是否存在都会调用类中的__getitem__()方法。而且返回值就是__getitem__()方法中规定的return值
        """获取属性"""
        data = self.data.get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name, item))


if __name__ == '__main__':
    search = GetYaml('recharge_data')
    print(search['新增'])

