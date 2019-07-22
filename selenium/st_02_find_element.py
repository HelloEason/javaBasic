# 如何使用 webdriver 定位元素

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw')
driver.find_element_by_class_name('s_ipt')
driver.find_element_by_name('wd')
driver.find_element_by_link_text(u'贴吧')
driver.find_element_by_partial_link_text(u'贴')
driver.find_element_by_tag_name('input')

# driver.find_element_by_xpath() 的各种用法 ：
driver.find_element_by_xpath('/html/body/div[2]/span/input')        #绝对路径
driver.find_element_by_xpath("//input[@attr='value']")              #元素属性定位
driver.find_element_by_xpath("//span[@id='kv']/span[2]/input")      #父元素层级定位
driver.find_element_by_xpath("//input[@id='kv' and @class='s_plt']") #逻辑运算定位

#CSS 定位：                                            #采用css 选择器的方式定位元素
driver.find_element_by_css_selector(".s_plt")
driver.find_element_by_css_selector("#kw")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input[attr='value']")

#By 定位 ，需指定定位方式和值
from selenium.webdriver.common.by import By
driver.find_element(By.ID,'kw')


