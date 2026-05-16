from features.pages.BasePage import BasePage
from features.pages.HomePage import HomePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    sign_in_jenkins_xpath = "//div[@class='app-sign-in-register__content-inner']/h1"
    username_id = "j_username"
    password_id = "j_password"
    submit_by_name = "Submit"
    submit_by_xpath = "//button[@name='Submit']"
    submit_by_css_selector = "button[type='submit']"
    login_error_by_css_selector = "div.app-sign-in-register__error"

    def on_login_page(self, expected_title):
        return self.get_page_title().__eq__(expected_title)

    def login_web_page(self, username, password):
        self.input_value(self.username_id, username)
        self.input_value(self.password_id, password)

    def click_submit(self):
        self.click_on_element("submit_by_css_selector", self.submit_by_css_selector)

        return HomePage(self.driver)

    def invalid_login(self,expected_error_message):
        element_text = self.validate_expected_element_innertext("login_error_by_css_selector",self.login_error_by_css_selector)
        return element_text == expected_error_message