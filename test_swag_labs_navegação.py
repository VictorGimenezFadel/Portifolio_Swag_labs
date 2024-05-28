"""
Navegação básica no site Swag Labs

Esse teste está em desenvolvimento
"""

# Import dos arquivos .py e das classes presentes dentro deles
from Pages.login_page import CL_LoginPage
from Pages.home_page import CL_HomePage, CL_MenuLateral, CL_OptnAbout, CL_IdentificarItens_ParaCarrinho, CL_AddItens_carrinho, CL_AcessarCarrinho
from Pages.carrinho_page import CL_IdentificarItens_carrinho, CL_RemoverItem_carrinho
from Pages.about_page import CL_VerificarPopUp, CL_FecharPopUp

from conftest import browser
import pytest


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



        # Verificar o PopUp - Página About (Sobre)
        verificar_popup = CL_VerificarPopUp(browser)
        verificar_popup.verificar_popup_pag_about()



        # Fechar o PopUp - Página About (Sobre)
        fechar_popup = CL_FecharPopUp(browser)
        fechar_popup.fechar_popup_pag_about()
        fechar_popup.voltar_pag_anterior() # Pega a ultima variável e aplica o método de voltar ou avançar para a página anterior



        # Adicionar itens ao carrinho - Página Home
        identificar_itens = CL_IdentificarItens_ParaCarrinho(browser) # Variavel para receber a class de identificação dos itens
        adicionar_itens = CL_AddItens_carrinho(browser) # Variavel para receber a class de adicionar os itens
        adicionar_itens.add_item_carrinho(identificar_itens) # Aplicar Variavel para receber o método de adição dos itens



        # 1° Acesso ao carrinho - Página Home
        carrinho = CL_AcessarCarrinho(browser)
        carrinho.entrar_carrinho()



        #1° Remoção de itens do carrinho
        identificar_itens = CL_IdentificarItens_carrinho(browser)  # Variavel para receber a class de identificação dos itens
        remover_itens = CL_RemoverItem_carrinho(browser)  # Variavel para receber a class de remoção dos itens
        remover_itens.remover_item_carrinho(identificar_itens)  # Aplicar Variavel para receber o método de remoção dos itens
        remover_itens.voltar_pag_anterior() # Pega a ultima variável e aplica o método de voltar ou avançar para a página anterior
