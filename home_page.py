""""
Interações / Configurações da página Home
"""""
from base_page import BasePage
from Testes.conftest import browser
from selenium.webdriver.common.by import By


class CL_HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")

    def verificar_login_bem_sucedido(self):
        # Verificar se o teste acessou a página inicial (Verifica o elemento do titulo da Home Page)
        self.verificar_se_elemento_existe(self.titulo_pagina)



class CL_MenuLateral(BasePage): # interação com o Menu lateral (3 risquinhos)
    def __init__(self, browser):
        super().__init__(browser)
        self.menu_lateral_esq = (By.ID, "react-burger-menu-btn") # Variavel que identifica o elemento

    def acessar_menu_lateral_esq(self):
        self.clicar(self.menu_lateral_esq)



class CL_OptnAbout(BasePage): # interação com a opção About (Sobre)
    def __init__(self, browser):
        super().__init__(browser)
        self.optn_about = (By.ID, "about_sidebar_link") # Variavel que identifica o elemento

    def acessar_about(self):
        self.clicar(self.menu_lateral_esq)
