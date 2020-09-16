from page.recharge_page import Recharge
import time
class TestAddRecharge():
    def test_click_recharge(self,driver,login):
        recharge = Recharge(driver)
        recharge.click_recharge()
        time.sleep(2)


    def test_click_add(self,driver,login):
        recharge = Recharge(driver)
        recharge.click_add()
        time.sleep(2)

    def test_click_add_recharge_way(self,driver,login):
        recharge = Recharge(driver)
        recharge.click_add_recharge_way()
        time.sleep(2)

    def test_click_sure(self,driver,login):
        Recharge(driver).click_sure()
        time.sleep(2)







