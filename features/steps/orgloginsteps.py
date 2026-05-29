from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
import time

@given('Launch chrome browser11')
def browser11(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('Open orangehrm homepage')
def open1(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(20)


@when('Enter valid "{user}" and valid "{pwd}"')
def enterus(context,user,pwd):
    context.driver.find_element(By.NAME,'username').send_keys(user)
    time.sleep(3)
    context.driver.find_element(By.NAME,'password').send_keys(pwd)
    time.sleep(3)


@when('Click on login button')
def click1(context):
    context.driver.find_element(By.XPATH, "//*[@type='submit']").click()
    time.sleep(3)

@then('Verify user login to the dashboard page')
def login1(context):
    context.driver.close()


@given('Launch chrome browser12')
def browser12(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('Enter invalid "{user1}" and invalid "{pwd1}"')
def enterus12(context,user1,pwd1):
    context.driver.find_element(By.NAME,'username').send_keys(user1)
    time.sleep(3)
    context.driver.find_element(By.NAME,'password').send_keys(pwd1)
    time.sleep(3)

@then('Verify user not login to the dashboard page')
def verify12(context):
    context.driver.close()
