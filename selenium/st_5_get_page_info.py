from selenium import webdriver
driver = webdriver.Chrome()
title = driver.title
url  = driver.current_url
text = driver.find_element_by_id('kw').text  # 获取元素信息
print(title, url, text)
