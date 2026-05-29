from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
import time

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)

#driver.find_element(By.NAME,"username").send_keys("Admin")


#driver.find_element(By.NAME,"password").send_keys("admin123")



#driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()















