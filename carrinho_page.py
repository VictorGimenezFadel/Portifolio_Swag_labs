""""
Interações / Configurações da página Carrinho
"""""
from base_page import BasePage
from Testes.conftest import browser
from selenium.webdriver.common.by import By


# 1° acesso a Página Carrinho
class CL_IdentificarItens_carrinho(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.btn_remover_item_bike_light = (By.ID, "remove-sauce-labs-backpack")
        self.btn_remover_item_onesie = (By.ID, "remove-sauce-labs-onesie")



class CL_RemoverItem_carrinho(BasePage):
    def remover_item_carrinho(self,identificar_itens):
        self.clicar(identificar_itens.btn_remover_item_bike_light)
        self.clicar(identificar_itens.btn_remover_item_onesie)
