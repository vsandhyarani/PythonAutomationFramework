from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

rd_male=driver.find_element(By.ID,"gender-male")
rd_female=driver.find_element(By.ID,"gender-female")
time.sleep(5)

print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()
time.sleep(5)

print(rd_male.is_selected())
print(rd_female.is_selected())




driver.quit()