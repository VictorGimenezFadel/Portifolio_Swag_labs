"""
Essa arquivo serve para criar métodos de verificação dos elementos, criar o assert e aplicar no arquivo principal
"""
from selenium.webdriver.common.by import By
from base_page import BasePage


class Cl_VerificarElementos_ItensCarrinho(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.item_verificar = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")

    def verificar_itens_presentes(self, nome_item):
        item = (self.item_verificar[0], self.item_verificar[1].format(nome_item))
        self.verificar_se_elemento_existe(item)



"""
class Cl_VerificarElementos_ItensCarrinho(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.item_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.item_bike_light = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.item_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

    def verificar_itens_presentes(self):
        for item_locator in [
            (By.ID, "add-to-cart-sauce-labs-backpack"),
            (By.ID, "add-to-cart-sauce-labs-bike-light"),
            (By.ID, "add-to-cart-sauce-labs-onesie"),
        ]:
            assert self.browser.find_element(*item_locator).is_displayed()
"""          
