from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
time.sleep(30)


windowids=driver.window_handles

for winid in windowids:
   driver.switch_to.window(winid)
   print(driver.title)
time.sleep(5)

for winid in windowids:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM":
        time.sleep(15)
        driver.close()


