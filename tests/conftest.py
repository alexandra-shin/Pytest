import os
import time
import pytest
from selenium import webdriver
from urllib3.exceptions import *
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class', params=["chrome"])
def driver(request):
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
                new_options.add_experimental_option("excludeSwitches", ["enable-automation"])
                # new_options.add_argument("--headless")        
                my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=new_options)        
                my_driver.maximize_window()
                my_driver.execute_cdp_cmd('Page.setDownloadBehavior', preferences)
                # my_driver.set_window_size(1920, 1080)
            elif browser == "firefox":
                new_options = FirefoxOptions()
                my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=new_options)
                my_driver.maximize_window()
            else:
                raise TypeError(f"Expected 'chrome' or 'edge', but got {browser}")
            my_driver.implicitly_wait(10)
            break
        except (Exception, NewConnectionError, ConnectionRefusedError):
            print("Caught an exception! Trying to initialize WebDriver again.")
            i += 1
            continue

    yield my_driver

    print(f"\nClosing {browser} driver")
    time.sleep(3)
    my_driver.quit()  
