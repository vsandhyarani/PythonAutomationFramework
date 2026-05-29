from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(10)

driver.find_element(By.XPATH,"//*[contains(@name,'username')]").send_keys("Admin")
time.sleep(10)

driver.find_element(By.XPATH,"//*[starts-with(@name,'password')]").send_keys("admin123")
time.sleep(10)

driver.find_element(By.XPATH,"//*[text()='OrangeHRM, Inc']").click()
time.sleep(10)