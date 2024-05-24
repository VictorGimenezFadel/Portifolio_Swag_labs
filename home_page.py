""""
SEÇÃO 07
home_page.py
"""""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base_page import CL_BasePage
from Testes.conftest import browser
from selenium.webdriver.common.by import By


class CL_HomePage(CL_BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")

    def verificar_login_bem_sucedido(self):
        # Verificar se o teste acessou a página inicial (Verifica o elemento do titulo da Home Page)
        self.verificar_se_elemento_existe(self.titulo_pagina)

class CL_MenuLateral(CL_BasePage): # interação com o Menu lateral (3 risquinhos)
    def __init__(self, browser):
        super().__init__(browser)
        self.menu_lateral_esq = (By.ID, "react-burger-menu-btn")

    def acessar_menu_lateral_esq(self):
        self.clicar(self.menu_lateral_esq)
      
