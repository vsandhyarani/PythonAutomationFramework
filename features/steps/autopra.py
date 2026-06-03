from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

@given('Launch the chrome browser')
def launch_browser(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(options=chrome_options)
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