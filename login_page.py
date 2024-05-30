"""
Interações / Configurações da página de Login
"""
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class CL_LoginInvalido(BasePage):

    def __init__(self, browser):
        super().__init__(browser) # Necessário para inicializar corretamente a BasePage
        self.campo_username = (By.ID, "user-name")
        self.campo_password = (By.ID, "password")
        self.btn_login = (By.ID, "login-button")
        self.mensagem_erro_login_invalido = (By.XPATH, "//*[@data-test='error']")


    def fazer_login_invalido(self, usuario, senha):
        # Interação com o Campo de username
        self.escrever(self.campo_username, usuario) # Escrever no campo de usuário, um usuário válido

        # Interação com o Campo de password
        self.escrever(self.campo_password, senha) # Escrever no campo de senha, uma senha válida

        # interação com o Botão de login
        self.clicar(self.btn_login) # Clicar no botão de login


    def verificar_mensagem_de_erro_login(self):
        self.verificar_se_elemento_existe(self.mensagem_erro_login_invalido)



class CL_LoginValido:

    def __init__(self, browser):
        self.browser = browser

    def fazer_login(self, usuario, senha):

        #Interação com o Campo de username
        username = self.browser.find_element(By.ID, "user-name")
        username.send_keys(usuario)

        #Interação com o Campo de password
        password = self.browser.find_element(By.ID, "password")
        password.send_keys(senha)

        #interação com o Botão de login
        btn_login = self.browser.find_element(By.ID, "login-button")
        btn_login.click()
