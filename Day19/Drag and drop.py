from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

act=ActionChains(driver)


driver.get("https://history.state.gov/countries/all")
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='content-inner']/div/div[1]/div[9]/ul/li[2]/a")
time.sleep(30)



