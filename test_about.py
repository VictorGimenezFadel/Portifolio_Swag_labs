"""
Navegação básica no site Swag Labs - Interações dentro da página about

Esse teste está em desenvolvimento
"""
# Import dos arquivos .py e das classes presentes dentro deles
import pytest
from conftest import browser
from about_page import (
    CL_VerificarPopUp,
    CL_FecharPopUp
)
from home_page import (
    CL_HomePage,
    CL_MenuLateral,
    CL_OptnAbout,
)
from login_page import (
    CL_LoginValido,
)


@pytest.mark.usefixtures("browser")
@pytest.mark.about  # mark para executar o teste através do pytest
class TestCT03_SwagLabs_about:
    def test_ct03_swaglabs_about(self, browser):
        # Tela de login

        # Login
        login_valido = CL_LoginValido(browser)
        login_valido.fazer_login("standard_user", "secret_sauce")



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



        # Verificar o PopUp - Página About (Sobre)
        verificar_popup = CL_VerificarPopUp(browser)
        verificar_popup.verificar_popup_pag_about()



        # Fechar o PopUp - Página About (Sobre)
        fechar_popup = CL_FecharPopUp(browser)
        fechar_popup.fechar_popup_pag_about()
        fechar_popup.voltar_pag_anterior()  # Pega a ultima variável e aplica o método de voltar ou avançar para a página anterior
