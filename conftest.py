""""
Configurações do browser
"""
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

    yield browser

    #Teardown
    browser.quit()
    
