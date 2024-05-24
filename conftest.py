""""
SEÇÃO 07 - Criando método para verificar se elemento existe na tela
conftest.py
"""
import pytest
from selenium import webdriver


@pytest.fixture
def browser():

    # Setup
    browser = webdriver.Edge()
    browser.implicitly_wait(15)
    browser.maximize_window()
    browser.get("https://www.saucedemo.com/")

    yield browser

    # Teardown
    browser.quit()
