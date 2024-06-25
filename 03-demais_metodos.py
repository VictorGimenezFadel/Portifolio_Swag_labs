"""
Essa arquivo serve para métodos alternativos para uma mesma funcionalidade
"""

# O TRECHO DESSE MÉTODO SERVE PARA REALIZAR A VERIFICAÇÃO DE MULTIPLOS ITENS

from selenium.webdriver.common.by import By
from base_page import BasePage


class Cl_VerificarElementos_ItensCarrinho_Verif01(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.item_backpack = (By.XPATH, "//a[@href='#' and @id='item_4_title_link']")
        self.item_bike_light = (By.XPATH, "//a[@href='#' and @id='item_0_title_link']")
        self.item_onesie = (By.XPATH, "//a[@href='#' and @id='item_2_title_link']")

    def verificar_itens_presentes_Verif01(self):
        for item_locator in [
            (By.XPATH, "//a[@href='#' and @id='item_4_title_link']"),
            (By.XPATH, "//a[@href='#' and @id='item_0_title_link']"),
            (By.XPATH, "//a[@href='#' and @id='item_2_title_link']"),
        ]:
            assert self.browser.find_element(*item_locator).is_displayed()





# ESSE MÉTODO SERVE PARA DINAMIZAR A ADIÇÃO DE ITENS AO CARRINHO ATRAVÉS DO TEXTO (TITULO DO PRODUTO)

class CL_AdicionarItens_carrinho(BasePage):  # 01 = 1° Identificação de itens para o carrinho
    def __init__(self, browser):
        super().__init__(browser)
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name ' and text()='{}']")
        self.carrinho = (By.XPATH, "//*[text()='Add to cart']")

    def add_ao_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1])
