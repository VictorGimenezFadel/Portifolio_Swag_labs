"""
Interações / Configurações dentro da info dos produtos
"""

from base_page import BasePage
from conftest import browser
from selenium.webdriver.common.by import By

# Voltar para os produtos
class CL_VoltarPara_Produtos(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.btn_voltar_para_produtos = (By.ID, "back-to-products")

    def voltar_para_produtos(self):
        self.clicar(self.btn_voltar_para_produtos)
      
