from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//*[@name='username']").send_keys("Admin")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@name='password']").send_keys("admin123")
time.sleep(5)


driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

time.sleep(5)
print(driver.title)
time.sleep(5)

act_title=driver.title



if act_title=="OrangeHRM":
    print("login is successful")
else:
    print("login failed")