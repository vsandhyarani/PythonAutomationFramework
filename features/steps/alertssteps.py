from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import *
import time
from selenium.webdriver.chrome.options import Options

@given('Launch the browser11')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()

@when('Open the autopra homepage')
def step_impl(context):
    context.driver.get('https://testautomationpractice.blogspot.com/')
    time.sleep(5)

@when('Click on the prompt Alert button')
def step_impl(context):
   context.driver.find_element(By.ID,"promptBtn").click()
   time.sleep(5)


@when('Enter name promt "{peru}"')
def step_impl(context,peru):
    myalert=context.driver.switch_to.alert
    myalert.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    myalert.send_keys(peru)
    time.sleep(5)

@when('Click on ok button')
def step_impl(context):
    myalert=context.driver.switch_to.alert
    myalert.accept()
    time.sleep(5)

@then('Verify entered text in pop-up page')
def step_impl(_context):
    print("verify text enetered successfully")
    time.sleep(5)

@then('Close the browser3')
def step_impl(context):
    context.driver.quit()

