from selenium import webdriver
import time

import os

driver=webdriver.Chrome()


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.sleep(10)


