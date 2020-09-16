from common.base import Base
from common.get_yaml import GetYaml
from data.recharge_data import *
import time
recharge = GetYaml('recharge_data')
class Recharge(Base):
    def click_recharge(self):
        '''
        点击收银台
        :return:
        '''
        time.sleep(3)
        self.click(recharge['点击收银台'])
    def click_add(self):
        '''
        点击新增
        :return:
        '''
        time.sleep(2)
        self.click(recharge['新增'])
    def click_add_recharge_way(self):
        '''
        点击新增
        :return:
        '''
        time.sleep(2)
        self.send(recharge['充值方式'],testdata['recharge_way'])
    def click_sure(self):
        '''
        点击确定
        :return:
        '''
        time.sleep(2)
        self.click(recharge['确定'])



