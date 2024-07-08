""""
Configurações do browser
"""
import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    # Setup
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get("https://www.saucedemo.com/")
    WebDriverWait(browser, 60)

    yield browser

    time.sleep(5)

    # Teardown
    browser.quit()
