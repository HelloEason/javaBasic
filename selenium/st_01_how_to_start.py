#coding=utf-8
#selenium 使用步骤：
# 1 从selenium 导入 webdriver 句柄
# 2 使用seltnium 获得 浏览器 驱动
# 3 使用驱动打开链接
# 4 查找页面元素进行操作
# 5 关闭浏览器

from selenium import webdriver
import  time

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options,desired_capabilities=None)

driver.get("http://www.baidu.com")

driver.find_element_by_xpath("//input[@id='kw']").send_keys('hello world')
tbotton = driver.find_element_by_id('su')
tbotton.click()

time.sleep(5)
driver.close()


