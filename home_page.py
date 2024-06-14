""""
Interações / Configurações da página Home
"""""
from Pages.base_page import BasePage
from conftest import browser
from selenium.webdriver.common.by import By


# 1° acesso a Página Home
class CL_HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")

    def verificar_login_bem_sucedido(self):
        self.verificar_se_elemento_existe(self.titulo_pagina) # Verificar se o teste acessou a página inicial (Verifica o elemento do titulo da Home Page)



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
        self.clicar(self.optn_about)



# 2° acesso a Página Home - ADD itens ao carrinho
class CL_IdentificarItens_ParaCarrinho_Ident01(BasePage):# 01 = 1° Identificação de itens para o carrinho
    def __init__(self, browser):
        super().__init__(browser)
        self.btn_add_item_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.btn_add_item_bike_light = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.btn_add_item_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")



class CL_AddItens_carrinho_Add01(BasePage): # 01 = 1° Primeira adição de itens ao carrinho
    def add_item_carrinho_01(self,identificar_itens_01):
        self.clicar(identificar_itens_01.btn_add_item_backpack)
        self.clicar(identificar_itens_01.btn_add_item_bike_light)
        self.clicar(identificar_itens_01.btn_add_item_onesie)



# 1° Acesso ao carrinho
class CL_AcessarCarrinho(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.icone_carrinho = (By.CLASS_NAME, "shopping_cart_link")

    def entrar_carrinho(self):
        self.clicar(self.icone_carrinho)



#
# 3° acesso a Página Home - ADD itens ao carrinho
class CL_IdentificarItens_ParaCarrinho_Ident02(BasePage):# Int02 = 2° Identificação de itens para o carrinho
    def __init__(self, browser):
        super().__init__(browser)
        self.btn_add_item_fleece_jacket = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        self.btn_add_item_bolt_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")



class CL_AddItens_carrinho_Add02(BasePage): # 02 = 2° Primeira adição de itens ao carrinho
    def add_item_carrinho_02(self,identificar_itens_02):
        self.clicar(identificar_itens_02.btn_add_item_fleece_jacket)
        self.clicar(identificar_itens_02.btn_add_item_bolt_tshirt)



# 2° Acesso ao carrinho
class CL_AcessarCarrinho(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.icone_carrinho = (By.CLASS_NAME, "shopping_cart_link")

    def entrar_carrinho(self):
        self.clicar(self.icone_carrinho)
