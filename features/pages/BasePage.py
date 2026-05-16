from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def get_element(self,locator_type,locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, locator_value)))
        elif locator_type.endswith("_name"):
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locator_value)))
        elif locator_type.endswith("_class_name"):
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, locator_value)))
        elif locator_type.endswith("_link_text"):
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, locator_value)))
        elif locator_type.endswith("_css_selector"):
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator_value)))
        elif locator_type.endswith("_xpath"):
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, locator_value)))
        elif locator_type.endswith("_tag_name"):
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, locator_value)))
        elif locator_type.endswith("_partial_link_text"):
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, locator_value)))
        return element

    def click_on_element(self,locator_type,locator_value):
        element = self.get_element(locator_type,locator_value)
        element.click()

    def input_value(self,locator_value,value):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, locator_value)))
        element.click()
        element.clear()
        element.send_keys(value)

    def validate_expected_element_text(self,locator_type,locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.text

    def validate_expected_element_innertext(self,locator_type,locator_value):
        element = self.get_element(locator_type, locator_value)
        #print(element.get_attribute("innerText"))
        return element.get_attribute("innerText")

    def validate_element_text_is_displayed(self,locator_type,locator_value,expected_element_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__eq__(expected_element_text)

    def validate_element_innertext_is_displayed(self,locator_type,locator_value,expected_element_text):
        element = self.get_element(locator_type, locator_value)
        #print(element.get_attribute("innerText"))
        return element.get_attribute("innerText").__eq__(expected_element_text)

    def get_page_title(self):
        return self.driver.title