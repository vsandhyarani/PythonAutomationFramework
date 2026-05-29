from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('launch chrome browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    time.sleep(5)

@when('open orangehrm homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(20)

@then('verify logo present in the orangehrm homepage')
def verifylogo(context):
    logo = context.driver.find_element(By.XPATH,"//img[@alt='company-branding']")
    assert logo.is_displayed()

@then('close the browser')
def closebrowser(context):
    time.sleep(3)
    context.driver.quit()
