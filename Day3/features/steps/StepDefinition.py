from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
@given(u'Login page')
def step_impl(context):
    # context.chrome_driver_path = r"F:\chromedriver_win64\chromedriver.exe"
    # context.chrome_options = Options()
    # context.chrome_options.add_argument("--start-maximized")
    # context.chrome_service = Service(context.chrome_driver_path)
    context.driver = webdriver.Chrome()
    context.driver.get("https://practicetestautomation.com/practice-test-login/")

@when(u'user enter valid username')
def step_impl(context):
    username = context.driver.find_element(By.XPATH,"//input[@name='username']")
    username.send_keys("student")

@when(u'user enter valid password')
def step_impl(context):
    password = context.driver.find_element(By.XPATH,"//input[@name='password']")
    password.send_keys("Password123")

@when(u'user click submit button')
def step_impl(context):
    submit = context.driver.find_element(By.XPATH,"//button[@id='submit']")
    submit.click()

@then(u'user enters to profile page')
def step_impl(context):
    print("Passed")


# @then(u'user is displayed')
# def step_impl(context):
#
#
# @then(u'log out button is displayed')
# def step_impl(context):


# @when(u'user enter invalid username "noStudent"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When user enter invalid username "noStudent"')
#
#
# @then(u'error message is displayed')
# def step_impl(context):
#
#
#
# @then(u'error text is "Your username is invalid!"')
# def step_impl(context):
#
#
# @when(u'user enter invalid password "Pass123"')
# def step_impl(context):
#
#
# @then(u'error text is "Your password is invalid!"')
# def step_impl(context):
