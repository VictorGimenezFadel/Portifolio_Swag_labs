""""
Interações / Configurações da página Carrinho
"""""
from base_page import BasePage
from conftest import browser
from selenium.webdriver.common.by import By


class CL_RemoverItens_Carrinho(BasePage):  # 01 = 1° Identificação de itens para o carrinho
    def __init__(self, browser):
        super().__init__(browser)
        self.item_carrinho = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.btn_remover_carrinho = (By.ID, "remove")

    def remover_item_carrinho(self, nome_item):
        item = (self.item_carrinho[0], self.item_carrinho[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.btn_remover_carrinho)


class CL_ContinueShopping(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.btn_continue_shopping = (By.ID, "continue-shopping")

    def continue_shopping_carrinho(self):
        self.clicar(self.btn_continue_shopping)


class CL_RealizarCheckout(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.btn_checkout = (By.ID, "checkout")

    def realizar_checkout_carrinho(self, realizar_checkout):
        self.clicar(realizar_checkout.btn_checkout)
