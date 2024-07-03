""""
Interações / Configurações da página Checkout
"""""
from base_page import BasePage
from conftest import browser
from selenium.webdriver.common.by import By


class CL_InfosCheckout(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.campo_first_name = (By.ID, "first-name")
        self.campo_last_name = (By.ID, "last-name")
        self.campo_postal_code = (By.ID, "postal-code")

    def inserir_infos(self, First_name, Last_name, Postal_code):
        # Interação com o Campo First Name
        self.escrever(self.campo_first_name, First_name)  # Escrever o primeiro nome

        # Interação com o Campo Last Name
        self.escrever(self.campo_last_name, Last_name)  # Escrever o último nome

        # interação com o Campo Postal Code
        self.escrever(self.campo_postal_code, Postal_code)  # Escrever o código postal


class CL_ContinueCheckout(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.btn_continue_checkout = (By.ID, "continue")

    def continuar_checkout(self):
        self.clicar(self.btn_continue_checkout)


class CL_FinalizarCheckout(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.btn_finish_checkout = (By.ID, "finish")

    def finalizar_checkout(self):
        self.clicar(self.btn_finish_checkout)


class CL_Voltar_PagInicial(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.btn_back_home = (By.ID, "back-to-products")

    def voltar_pagina_incial(self):
        self.clicar(self.btn_back_home)
      
