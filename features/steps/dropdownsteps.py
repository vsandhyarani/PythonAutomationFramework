from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from behave import *
import time

@given('Launch the chrome browser1')
def browser1(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()


@when('Open autopra homepage')
def open_autopra(context):
   context.driver.get("https://testautomationpractice.blogspot.com/")
   time.sleep(5)


@when('Click and select the dropdown icon')
def click_dropdown(context):
    drop_country=Select(context.driver.find_element(By.ID,"country"))
    time.sleep(10)
    alloptions=drop_country.options
    for option in alloptions:
        if option.text=="Japan":
            option.click()
    time.sleep(10)

@then('Verify user selected the country from dropdown')
def verify_dropdown(_context):
    print("successfully select the country from dropdown")
    time.sleep(5)

@then('Close the browser2')
def close_browser2(context):
 context.driver.quit()