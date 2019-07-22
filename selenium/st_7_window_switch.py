from selenium import webdriver
driver = webdriver.Chrome()
handle = driver.current_window_handle
handles = driver.window_handles
driver.switch_to_window()
driver.switch_to.window(handles[2])


