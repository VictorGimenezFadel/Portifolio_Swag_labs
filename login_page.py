"""
Login do Swag Labs

TIME SLEEP É SOMENTE PARA UMA VISUALIZAÇÃO QUE SIMULA UMA NAVEGAÇÃO DE UM USUÁRIO
"""

import time
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def fazer_login(self, usuario, senha):

        #Interação com o Campo de username
        username = self.browser.find_element(By.ID, "user-name")
        username.send_keys(usuario)
        time.sleep(1)

        #Interação com o Campo de password
        password = self.browser.find_element(By.ID, "password")
        password.send_keys(senha)
        time.sleep(1)

        #interação com o Botão de login
        btn_login = self.browser.find_element(By.ID, "login-button")
        btn_login.click()
        time.sleep(1)
      
