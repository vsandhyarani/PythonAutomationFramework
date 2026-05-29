from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
import time

@given('Launch the chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('Open the homepage')
def open_homepage(context):
    context.driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(3)
    context.driver.maximize_window()
    time.sleep(10)

@when('Enter name "{user}" and Enter email "{email}" and phone "{contact}"')
def enter_cred(context,user,email,contact):
    context.driver.find_element(By.ID,"name").send_keys(user)
    time.sleep(3)
    context.driver.find_element(By.ID,"email").send_keys(email)
    time.sleep(3)
    context.driver.find_element(By.ID,"phone").send_keys(contact)
    time.sleep(3)

@then('Close the browser')
def close_browser(context):
    context.driver.close()