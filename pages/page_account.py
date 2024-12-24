from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.common_helpers import Helpers
from pages.constants import *

class AccountPage:

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.common = Helpers(self._driver)

        self.url_account = f"{constant_base_url}/my-account/"
        self.url_security = f"{constant_base_url}/my-account/security-settings"
        self.dropdown_month = (By.ID, "customer_birthday_month")
        self.dropdown_day = (By.ID, "customer_birthday_day")
        self.dropdown_year = (By.ID, "customer_birthday_year")

    def go_to_account_page(self):
        self._driver.get(self.url_account)
        return self

    def change_dob(self, month: str, day: str, year: str): 
        self.common.select_from_dropdown(self.dropdown_month, month, wait_after_sec = 2)
        self.common.select_from_dropdown(self.dropdown_day, day, wait_after_sec = 2)
        self.common.select_from_dropdown(self.dropdown_year, year, wait_after_sec = 2)
        return self

    def assert_dob_is_changed(self, month, day, year) -> bool:
        self._driver.get(self.url_security)
        self._driver.get(self.url_account)

        def get_selected_option(option: str) -> str:
            return self.common.get_text((By.XPATH, f"//option[text()='{option}']/following-sibling::option[@selected='selected']"))
        
        assert (get_selected_option('Month') == month \
                and get_selected_option('Day') == day \
                and get_selected_option('Year') == year)
        return self
