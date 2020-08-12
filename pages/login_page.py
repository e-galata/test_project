from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
	    assert LoginPageLocators.LOGIN_URL in self.browser.current_url, "Login url is not correct"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_UP), "Login form is not presented"
        # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_IN), "Register form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
		
    def register_new_user(self, browser, email, password):
        self.should_be_register_form()
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_field.send_keys(email)
        passwd = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        passwd.send_keys(password)
        passwd2 = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD)
        passwd2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()