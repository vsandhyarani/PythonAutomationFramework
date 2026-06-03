from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('launch chrome browser')
def launchbrowser(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    time.sleep(5)

@when('open orangehrm homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(20)

@then('verify logo present in the orangehrm homepage')
def verifylogo(context):
    logo = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//img[contains(@alt,'company')]")
        )
    )

    assert logo.is_displayed()

@then('close the browser')
def closebrowser(context):
    time.sleep(3)
    context.driver.quit()
