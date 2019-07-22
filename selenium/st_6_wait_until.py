from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import  time
driver = webdriver.Chrome()
element = WebDriverWait(driver,5,1).until(EC.presence_of_element_located((By.ID,'kw'))) # 显式等待

driver.implicitly_wait(10) # 隐式等待

time.sleep(5)       # 休眠等待
