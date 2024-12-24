from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.common_helpers import Helpers
from pages.constants import *

class LoginPage:

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.common = Helpers(self._driver)

        self.url = f"{constant_base_url}/signin"
        self.input_email = (By.ID, "signInEmailInput")
        self.input_password = (By.ID, "signInPasswordInput")
        self.button_sign_in = (By.XPATH, "//button[text()='Sign In']")
        self.success_message = (By.XPATH, "//span[text()='Sasha']")
        self.error_message = (By.XPATH, "//div[contains(text(), 'not correct')]")

    def go_to_login_page(self):
        self._driver.get(self.url)
        return self

    def login(self, username, password): 
        self.common.clear_textfield_and_type(self.input_email, username)
        self.common.clear_textfield_and_type(self.input_password, password)
        self.common.click_and_wait(self.button_sign_in, 1, 4)
        return self

    def assert_is_logged_in(self):
        assert self.common.is_displayed(self.success_message)
        
    def assert_is_login_failed(self):
        assert self.common.is_displayed(self.error_message)
    