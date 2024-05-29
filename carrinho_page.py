""""
Interações / Configurações da página Carrinho
"""""
from base_page import BasePage
from Testes.conftest import browser
from selenium.webdriver.common.by import By


# 1° acesso a Página Carrinho
class CL_IdentificarItens_carrinho_01(BasePage): # 01 = 1° Identificação de itens dentro do carrinho
    def __init__(self, browser):
        super().__init__(browser)
        self.btn_remover_item_bike_light = (By.ID, "remove-sauce-labs-backpack")
        self.btn_remover_item_onesie = (By.ID, "remove-sauce-labs-onesie")



class CL_RemoverItem_carrinho_01(BasePage): # 01 = 1° Remoção de itens dentro do carrinho
    def remover_item_carrinho_01(self,remover_item):
        self.clicar(remover_item.btn_remover_item_bike_light)
        self.clicar(remover_item.btn_remover_item_onesie)
        


class CL_IdentificarBtn_checkout(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.btn_checkout = (By.ID, "checkout")



class CL_RealizarCheckout(BasePage):
    def realizar_checkout_carrinho(self, realizar_checkout):
    self.clicar(realizar_checkout.btn_checkout)
    
