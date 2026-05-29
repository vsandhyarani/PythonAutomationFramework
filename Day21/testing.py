from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By


import time



driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)


tab=driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[2]/td[2]")
time.sleep(5)
act=ActionChains(driver)

act.move_to_element(tab).perform()
time.sleep(5)





