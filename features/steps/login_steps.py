from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.pages.LoginPage import LoginPage
from utilities import ReadConfigurations


@given("the user is on the Google login page")
def step_impl(context):
    context.driver.get(ReadConfigurations.read_configurations("basic info",'url1'))

@given("the user is on the Jenkins login page")
def step_impl(context):
    login_page_title = "Sign in - Jenkins"
    context.login_page = LoginPage(context.driver)
    assert context.login_page.on_login_page(login_page_title)

@when("the user clicks gmail label to go mail page")
def step_impl(context):
    element = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Gmail ']")))
    element.click()

@when("the user enters {username} and {password}")
def step_impl(context, username, password):
    context.login_page.login_web_page(username, password)

@when("the user clicks login button")
def step_impl(context):
    context.home_page=context.login_page.click_submit()

@then("the user verifies gmail page")
def step_impl(context):
    element = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "TemplateHeader_headerLogos")))
    if element.is_displayed():
        print("Gmail page verified")
    else:
        assert False, "Gmail page verification failed"

@then("the user logins Jenkins successfully")
def step_impl(context):
    assert context.home_page.valid_login(), "Login jenkins failed!"

@then("the user logins Jenkins failed")
def step_impl(context):
    expected_error_message = "Invalid username or password"
    assert context.login_page.invalid_login(expected_error_message), "This user should not be able to login!"