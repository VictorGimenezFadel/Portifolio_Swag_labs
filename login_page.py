"""
ORGANIZAÇÃO DA login_page - COMANDOS DE LOGIN
login_page.py
"""
from selenium.webdriver.common.by import By
from BasePage import CL_BasePage


class CL_LoginPage(CL_BasePage):

    def __init__(self, browser):
        super().__init__(browser) # Necessário para inicializar corretamente a BasePage
        self.campo_username = (By.ID, "user-name")
        self.campo_password = (By.ID, "password")
        self.btn_login = (By.ID, "login-button")

    def fazer_login(self, usuario, senha):
        # Interação com o Campo de username
        self.escrever(self.campo_username, usuario) # Escrever no campo de usuário, um usuário válido

        # Interação com o Campo de password
        self.escrever(self.campo_password, senha) # Escrever no campo de senha, uma senha válida

        # interação com o Botão de login
        self.clicar(self.btn_login) # Clicar no botão de login
