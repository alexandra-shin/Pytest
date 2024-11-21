import time
from selenium.webdriver import ActionChains
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

"""
Here is the set of custom functions I created which help to interact with UI of web application.
"""
# Default wait time in seconds.
WAIT = 10

class BaseClass:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple, time: int = WAIT) -> WebElement:
        """ wait specifed time and locate the element """
        self._wait_until_element_is_visible(locator, time)
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = WAIT):
        """ wait specifed time and type text into the text area """
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def clear_textfield(self, locator: tuple):
        """ clear text field using clear() method """
        self._find(locator).clear()

    def clear_textfield_advanced(self, locator: tuple):
        """ clear text field using keys """
        self._find(locator).send_keys(Keys.CONTROL + "a")
        self._find(locator).send_keys(Keys.DELETE)

    def type_and_enter(self, locator: tuple, text: str):
        """ type something then enter """
        self._find(locator).send_keys(text, Keys.ENTER)

    def type_and_enter_advanced(self, locator: tuple, text: str, pause: int=None):
        """ type something, wait and then enter """
        self._find(locator).send_keys(text)
        if pause:
            time.sleep(pause) 
        self._find(locator).send_keys(Keys.ENTER)      

    def click(self, locator: tuple):
        """ look for the element and click """
        self._find(locator).click()

    def double_click(self, locator: tuple):
        ActionChains(self._driver).double_click(self._find(locator)).perform()
        ActionChains(self._driver).reset_actions()

    def right_click(self, locator: tuple):
        ActionChains(self._driver).context_click(self._find(locator)).perform()
        ActionChains(self._driver).reset_actions()

    def scroll_to_element(self, locator: tuple):
        """ move to a specific element on the page """
        ActionChains(self._driver).move_to_element(self._find(locator)).perform()
        ActionChains(self._driver).reset_actions()

    def scroll_to_element_advanced(self, locator: tuple, pause: int):
        """ move to a specific element on the page with wait time """
        ActionChains(self._driver) \
            .move_to_element(self._find(locator)) \
            .pause(pause) \
            .perform()
        ActionChains(self._driver).reset_actions()

    def drag_and_drop(self, locator_source: tuple, locator_target: tuple):
        """ drag'n'drop specific element to specific location on the page """
        ActionChains(self._driver).drag_and_drop(self._find(locator_source), self._find(locator_target)).perform()
        ActionChains(self._driver).reset_actions()

    def drag_and_drop_advanced(self, locator_source: tuple, pause: int, locator_target: tuple):
        """ drag'n'drop specific element to specific location on the page with wait time """
        ActionChains(self._driver) \
            .click_and_hold(self._find(locator_source)) \
            .move_to_element(self._find(locator_target)) \
            .pause(pause) \
            .release().perform()
        ActionChains(self._driver).reset_actions()

    def click_and_wait(self, locator: tuple, before: int, after: int):
        time.sleep(before)
        self._find(locator).click()
        time.sleep(after)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = WAIT):
        """ waits until the element is visible with a timeout """
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator), f"Element {locator} is not visible")

    def wait_until_found(self, locator: tuple, timeout: int = WAIT):
        """ wait until the element is found using the locator BUT not neceseraliy visble """
        wait = WebDriverWait(self._driver, timeout)
        wait.until(ec.presence_of_all_elements_located(locator), f"Element {locator} is not visible")

    def get_text(self, locator: tuple, time: int = WAIT) -> str:
        """ get visible text on the web page related to specific locator """
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def get_attribute(self, locator: tuple, attribute: str, time: int = WAIT) -> str:
        """ retrive the value of a specific attribute of a web element """
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).get_attribute(attribute)

    def select_from_dropdown(self, locator: tuple, text: str):
        Select(self._find(locator)).select_by_visible_text(text)

    @property
    def get_current_url(self) -> str:
        return self._driver.current_url

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self._driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def java_script_clicker(self, locator: tuple):
        b = self._driver.find_element(*locator)
        self._driver.execute_script("arguments[0].click();", b)

    def clean_cache_and_cookies(self):
        self._driver.delete_all_cookies()
        self._driver.refresh()

    def is_selected(self, locator: tuple) -> bool:
        return self._find(locator).is_selected()

    def is_enabled(self, locator: tuple) -> bool:
        return self._find(locator).is_enabled()

    def scroll_to_bottom_of_element(self, locator: tuple):
        element = self._driver.find_element(*locator)
        self._driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)
