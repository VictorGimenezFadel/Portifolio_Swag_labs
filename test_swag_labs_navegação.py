"""
Navegação básica no site Swag Labs

Esse teste está em desenvolvimento
"""
import time
import pytest
from Pages.login_page import CL_LoginPage  # Pages é a pasta onde está a login_page
from Pages.home_page import CL_HomePage, CL_MenuLateral,CL_OptnAbout, CL_FecharPopUp
from conftest import browser


@pytest.mark.usefixtures("browser")
@pytest.mark.navegar # mark para executar o teste através do pytest
class TestCT01_Swag_labs:
    def test_ct01_swaglabs_navegação(self, browser):

        # Primeiro Login
        login_page = CL_LoginPage(browser)
        login_page.fazer_login("standard_user", "secret_sauce")



        # Tela inicial - Home

        # Conexão com a home_page.py e os métodos dentro dela - Home Page
        home_page = CL_HomePage(browser)  # CL_LoginPage é a class la no arquivo login_page.py
        home_page.verificar_login_bem_sucedido()



        # Primeira interação com o Menu lateral (3 risquinhos) - Home Page
        menu_lateral_esq = CL_MenuLateral(browser)
        menu_lateral_esq.acessar_menu_lateral_esq()



        # Primeiro interação como o botão about (sobre)
        optn_about = CL_OptnAbout(browser)
        optn_about.acessar_about()



        # Fechar primeiro PopUp - Página About (Sobre)
        fechar_popup = CL_FecharPopUp(browser)
        fechar_popup.fechar_popup_pag_about()


        quit()
