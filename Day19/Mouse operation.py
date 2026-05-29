from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time

driver.get("https://testautomationpractice.blogspot.com/#")
driver.maximize_window()

point=driver.find_element(By.XPATH,"//*[@id='HTML3']/div[1]/div/button")
point1=driver.find_element(By.XPATH,"//*[@id='HTML3']/div[1]/div/div/a[1]")
point2=driver.find_element(By.XPATH,"//*[@id='HTML3']/div[1]/div/div/a[2]")
time.sleep(5)

act=ActionChains(driver)

act.move_to_element(point).move_to_element(point1).move_to_element(point2).click().perform()
time.sleep(2)