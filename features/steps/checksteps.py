from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

@given('Launch the Chrome Browser')
def launch(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    time.sleep(10)


@when('Open the automation homepage')
def automation(context):
    context.driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(10)

@when('Click the checkbox')
def click_checkbox(context):
    checkboxes=context.driver.find_elements(By.XPATH,"//*[contains(@id,'day')]")
    time.sleep(5)
    for i in range(len(checkboxes)):
        if i==5 or i==6:
            checkboxes[i].click()
            time.sleep(3)

@then('Close the browser1')
def close_browser1(context):
 context.driver.quit()