from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
btn = driver.find_elements_by_xpath("//*[text() = '收银台']")
ActionChains(driver).click(btn).perform()