# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get('http://m.mail.10086.cn')
driver.
time.sleep(3)
# driver.find_element_by_xpath("//input[@name='email']").clear()
driver.find_element_by_xpath("//*[@id='label_user']").send_keys('chenyijin')
# driver.find_element_by_xpath("//input[@name='password']").clear()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='txtPass']").send_keys('23456')


aim_ele = driver.find_element_by_id('kw')
ActionChains(driver).context_click(aim_ele).perform()
aim_ele.send_keys(Keys.CONTROL,Keys.ENTER,'C')


driver.find_elements_by_tag_name('input').pop().click() # 选择一组元素，pop 最后一个，进行操作

driver.switch_to_frame('frame_id_or_name')
driver.switch_to.frame('frame_id_or_name')
driver.switch_to.default_content()      # 返回上一级内容

driver.switch_to_alert().accept()
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()






