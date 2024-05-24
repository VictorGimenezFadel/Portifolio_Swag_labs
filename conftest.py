import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser():

    #Setup
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get("https://www.saucedemo.com/")
    WebDriverWait(browser, 60)
    time.sleep(1)

    yield browser

    #Teardown
    browser.quit()
  
