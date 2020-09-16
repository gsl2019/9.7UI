from selenium import webdriver
import pytest
import time
from common.read_config import ReadConfig
@pytest.fixture(scope="session")
def driver():
    """定义全局driver fixture"""
    driver = webdriver.Chrome()
    #窗口最大化
    driver.maximize_window()
    '''
    def end():
        """全部用例执行完后，关闭dirver"""
    time.sleep(3)
    driver.quit()
    """终结函数"""
    request.addfinalizer(end)
    '''
    return driver


@pytest.fixture(scope="session")
def login(driver):
    url = ReadConfig().get_value('host','host')
    driver.get(url)
    driver.add_cookie({'name': 'ADM_TOKEN', 'value': 'eaa269cb5a7709a3d5657ce662fc73885c06b4b8'})
    time.sleep(1)
    driver.refresh()
