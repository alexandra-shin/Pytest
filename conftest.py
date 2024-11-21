import os
import time
import pytest
from selenium import webdriver
from urllib3.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

""" My implementation of conftest """

@pytest.fixture(scope='function', params=["chrome"])
def driver(request):
    url = "https://your-domen-here.com:0000/"
    username = "your_username"
    password = "your_password"

    browser = request.param
    print(f"\nCreating {browser} driver")
    i = 0
    while i < 5:
        try:
            if browser == "chrome":
                new_options = webdriver.ChromeOptions()
                preferences = {
                     'behavior' : 'allow',
                     'downloadPath' : os.getcwd() 
                }
                new_options.add_argument("--incognito")
                new_options.add_argument("--disable-dev-shm-usage")
                new_options.add_argument("--no-sandbox")
                # new_options.add_argument("--headless")
                my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=new_options)        
                my_driver.maximize_window()
                my_driver.execute_cdp_cmd('Page.setDownloadBehavior', preferences)
                # my_driver.set_window_size(1920, 1080)
            elif browser == "edge":
                my_driver = webdriver.Edge()
            elif browser == "firefox":
                new_options = FirefoxOptions()
                my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=new_options)
                my_driver.maximize_window()
            else:
                raise TypeError(f"Expected 'chrome' or 'edge', but got {browser}")
            my_driver.implicitly_wait(10)

            my_driver.get(url)
            my_driver.find_element(By.ID, "UserName").send_keys(username)
            my_driver.find_element(By.ID, "Password").send_keys(password)
            my_driver.find_element(By.XPATH, "//button[@type='submit']").click()
            home_button = my_driver.find_element(By.XPATH, "//span[contains(text(),'Home')]")
            assert home_button.is_displayed(), "Home button should be visible"
            break
        except (Exception, NewConnectionError, ConnectionRefusedError):
            print("Caught an exception! Trying to initialize WebDriver again.")
            i += 1
            continue

    yield my_driver

    print(f"\nClosing {browser} driver")
    time.sleep(3)
    my_driver.quit()  
