""""
Interações / Configurações da página Home
"""""
from base_page import BasePage
from Testes.conftest import browser
from selenium.webdriver.common.by import By


# 1° acesso a Página Home
class CL_VerificarPopUp(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.popup_pag_about = (By.CLASS_NAME, "ot-sdk-row") #Verifica se o pop-up está visivel e pode ser clicavel

    def verificar_popup_pag_about(self):
        self.verificar_se_elemento_existe(self.popup_pag_about) # Verificar se o popup está presente antes fechar ele


class CL_FecharPopUp(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.popup_pag_about_fechar = (By.ID, "onetrust-accept-btn-handler")  # Verifica se o pop-up está visivel e pode ser clicavel

    def fechar_popup_pag_about(self):
        self.clicar(self.popup_pag_about_fechar)
