# coding=utf-8
from selenium import webdriver
import  time

driver = webdriver.Chrome()
driver.get('http://m.mail.10086.cn')
time.sleep(2)
driver.get('http://www.baidu.com')

driver.set_window_size(480,800)     #浏览器大小设置
driver.set_window_position(300,300)

time.sleep(3)
driver.back()       #浏览器后退
time.sleep(3)
driver.forward()    #浏览器前进




# time.sleep(3)
# driver.close()

