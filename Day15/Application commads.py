from selenium import webdriver
import time

driver=webdriver.Chrome()

#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#driver.maximize_window()

#print(driver.title)
#time.sleep(5)
#print(driver.current_url)
#print(driver.page_source)


driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
time.sleep(5)