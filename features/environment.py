import allure
from selenium import webdriver

from utilities import ReadConfigurations

def before_scenario(context, scenario):
    # Initialize the specific browser driver
    browser_name = ReadConfigurations.read_configurations('basic', 'browser')
    if browser_name == 'chrome':
        context.driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        context.driver = webdriver.Firefox()
    elif browser_name == 'edge':
        context.driver = webdriver.Edge()

    context.driver.get(ReadConfigurations.read_configurations("basic", 'url'))
    context.driver.maximize_window()



def after_scenario(context, scenario):
    # Ensure the driver closes after every scenario
    if context.driver:
        context.driver.quit()

def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name='failed_testcase_screenshot'
                      ,attachment_type=allure.attachment_type.PNG)
