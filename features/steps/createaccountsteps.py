from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('Launch the chrome browser9')
def browser9(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()
    time.sleep(3)

@when('Click on login button1')
def button1(context):

    context.driver.get("https://www.makemytrip.com/")
    context.driver.maximize_window()
    time.sleep(5)

    # Close the popup by clicking on empty space
    from selenium.webdriver.common.action_chains import ActionChains

    ActionChains(context.driver).move_by_offset(10, 10).click().perform()
    time.sleep(3)

    # Locate login button
    login = context.driver.find_element(
        By.XPATH,
        "//p[@data-cy='LoginHeaderText']"
    )

    # Click using JavaScript
    context.driver.execute_script(
        "arguments[0].click();",
        login
    )

    time.sleep(3)

@when('Enter mobileno "{mobileno}"')
def mobileno(context, mobileno):
    context.driver.find_element(By.XPATH,"//*[@id='header-container']/div[2]/div[2]/div/section/form/div[1]/div/input").send_keys(mobileno)
    time.sleep(30)


@when('Click on continue button')
def continue1(context):
    context.driver.find_element(By.XPATH,"//*[@id='header-container']/div[2]/div[2]/div/section/form/div[2]/button/span").click()
    time.sleep(3)

@then('User should created account1')
def account1(_context):
    print("successfully created account1")
