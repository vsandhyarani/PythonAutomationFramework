from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from behave import *

@given('Launch the chrome browser3')
def browsser3(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()
    time.sleep(3)


@when('Open the automation test practice')
def testpractice(context):
    context.driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(3)




@when('Move cursor to master in selenium')
def move_cursor(context):
    context.act=ActionChains(context.driver)
    scrolling=context.driver.find_element(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr[5]/td[1]")
    time.sleep(5)
    context.act.move_to_element(scrolling).perform()
    time.sleep(5)



@then('Verify cursor is scrolled')
def verify_cursor(context):
     print("Verify cursor is scrolled")
     time.sleep(3)
     context.driver.close()