from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(10)

checkboxes=driver.find_elements(By.XPATH,"//*[contains(@id,'day')]")

for i in range(len(checkboxes)):
    if i<2:
      checkboxes[i].click()

time.sleep(5)

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

time.sleep(5)













