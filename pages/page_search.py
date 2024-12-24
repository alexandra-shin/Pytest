from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.common_helpers import Helpers
from pages.constants import *
import time

class SearchPage:

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.common = Helpers(self._driver)

        self.url = constant_base_url
        self.input_search = (By.NAME, "query")
        self.success_found = (By.XPATH, "(//span[contains(text(), 'Oboz Bridger')])[1]")
        self.error_not_found = (By.XPATH, "(//div[contains(text(), 'No results')])")

    def go_to_search_page(self):
        self._driver.get(self.url)
        return self

    def search(self, item: str): 
        self.common.type_and_enter(self.input_search, item)
        time.sleep(2)
        return self

    def assert_item_found(self):
        assert self.common.is_displayed(self.success_found)
        
    def assert_item_not_found(self):
        assert self.common.is_displayed(self.error_not_found)


