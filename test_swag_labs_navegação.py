"""
Navegação básica no site Swag Labs

Esse teste está em desenvolvimento
"""
# Import dos arquivos .py e das classes presentes dentro deles
import pytest
from conftest import browser
from verificar_elementos import (
    Cl_VerificarElementos_ItensCarrinho_Verif01
)
from login_page import (
    CL_LoginValido,
    CL_LoginInvalido,
)
from home_page import (
    CL_HomePage,
    CL_MenuLateral,
    CL_OptnAbout,
    #CL_IdentificarItens_ParaCarrinho_Ident01,
    CL_AddItens_carrinho_Add01,
    CL_IdentificarItens_ParaCarrinho_Ident02,
    CL_AddItens_carrinho_Add02,
    CL_AcessarCarrinho,
)
from carrinho_page import (
    CL_IdentificarBtn_RemoverCarrinho_01,
    CL_RemoverItem_carrinho_01,
)
from about_page import (
    CL_VerificarPopUp,
    CL_FecharPopUp
)



@pytest.mark.usefixtures("browser")
@pytest.mark.navegar # mark para executar o teste através do pytest


class TestCT01_Swag_labs:
    def test_ct01_swaglabs_navegação(self, browser):

        # Tela de login

        # Primeiro Login - Inválido
        login_invalido = CL_LoginInvalido(browser)
        login_invalido.fazer_login_invalido("standard_user", "senha_errada")
        login_invalido.verificar_mensagem_de_erro_login()
        login_invalido.recarregar_pagina()



        # Primeiro Login - Válido
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
        fechar_popup.voltar_pag_anterior() # Pega a ultima variável e aplica o método de voltar ou avançar para a página anterior



        # 1° Adição de itens ao carrinho - Página Home
        identificar_itens_01 = CL_IdentificarItens_ParaCarrinho_Ident01(browser) # Variavel para receber a class de identificação dos itens
        adicionar_itens_01 = CL_AddItens_carrinho_Add01(browser) # Variavel para receber a class de adicionar os itens
        adicionar_itens_01.adicionar_itens_carrinho_01(identificar_itens_01) # Aplicar Variavel para receber o método de adição dos itens



        # 1° Acesso ao carrinho - Página Home
        carrinho = CL_AcessarCarrinho(browser)
        carrinho.entrar_carrinho()



        # 1° Primeira verificação de itns do carrinho - Carrinho

        assert resultado_verificacao_01, "Elementos do carrinho não estão presentes!" #Essa menssagem irá aparecer caso o testde falhar



        #1° Remoção de itens do carrinho - Carrinho
        identificar_itens_01 = CL_IdentificarBtn_RemoverCarrinho_01(browser)  # Variavel para receber a class de identificação dos itens
        remover_itens = CL_RemoverItem_carrinho_01(browser)  # Variavel para receber a class de remoção dos itens
        remover_itens.remover_item_carrinho_01(identificar_itens_01)  # Aplicar Variavel para receber o método de remoção dos itens
        remover_itens.voltar_pag_anterior() # Pega a ultima variável e aplica o método de voltar ou avançar para a página anterior



        # 2° Adição de itens ao carrinho - Página Home
        identificar_itens_02 = CL_IdentificarItens_ParaCarrinho_Ident02(browser) # Variavel para receber a class de identificação dos itens
        adicionar_itens_02 = CL_AddItens_carrinho_Add02(browser) # Variavel para receber a class de adicionar os itens
        adicionar_itens_02.adicionar_itens_carrinho_02(identificar_itens_02)



        # 2° Acesso ao carrinho - Página Home
        carrinho = CL_AcessarCarrinho(browser)
        carrinho.entrar_carrinho()
