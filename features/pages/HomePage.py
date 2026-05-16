from features.pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    jenkins_css_selector = "span.jenkins-mobile-hide"

    def  valid_login(self):
        return self.validate_element_innertext_is_displayed("jenkins_css_selector",self.jenkins_css_selector,"Jenkins")