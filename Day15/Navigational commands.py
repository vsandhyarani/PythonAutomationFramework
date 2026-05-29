from selenium import webdriver
import time


driver=webdriver.Chrome()

driver.get("https://www.amazon.com/")
driver.maximize_window()
driver.get("https://www.myntra.com/")
driver.maximize_window()

time.sleep(2)

driver.back()
driver.forward()
time.sleep(2)

driver.refresh()

driver.quit()





