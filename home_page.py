""""
Interações / Configurações da página Home
"""""
from base_page import BasePage
from conftest import browser
from selenium.webdriver.common.by import By


# Verificar login bem sucedido
class CL_HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")

    def verificar_login_bem_sucedido(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)  # Verificar se o teste acessou a página inicial (Verifica o elemento do titulo da Home Page)


# Acessar menu lateral - Canto superior esquerdo
class CL_MenuLateral(BasePage):  # interação com o Menu lateral (3 risquinhos)
    def __init__(self, browser):
        super().__init__(browser)
        self.menu_lateral_esq = (By.ID, "react-burger-menu-btn")  # Variavel que identifica o elemento

    def acessar_menu_lateral_esq(self):
        self.clicar(self.menu_lateral_esq)


# Acessar opção About
class CL_OptnAbout(BasePage):  # interação com a opção About (Sobre)
    def __init__(self, browser):
        super().__init__(browser)
        self.optn_about = (By.ID, "about_sidebar_link")  # Variavel que identifica o elemento

    def acessar_about(self):
        self.clicar(self.optn_about)


# Adicionar itens ao carrinho
class CL_AdicionarItens_Carrinho(BasePage):  # 01 = 1° Identificação de itens para o carrinho
    def __init__(self, browser):
        super().__init__(browser)
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name ' and text()='{}']")
        self.btn_adicionar_carrinho = (By.ID, "add-to-cart")

    def add_ao_carrinho(self,nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.btn_adicionar_carrinho)


# Acessar o carrinho
class CL_AcessarCarrinho(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.icone_carrinho = (By.CLASS_NAME, "shopping_cart_link")

    def entrar_carrinho(self):
        self.clicar(self.icone_carrinho)
