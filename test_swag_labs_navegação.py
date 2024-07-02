"""
Navegação básica no site Swag Labs

Esse teste está em desenvolvimento
"""
# Import dos arquivos .py e das classes presentes dentro deles
import pytest
from conftest import browser
from about_page import (
    CL_VerificarPopUp,
    CL_FecharPopUp
)
from carrinho_page import (
    CL_RemoverItens_Carrinho,
    CL_ContinueShopping,
    # CL_IdentificarBtn_RemoverCarrinho_01,
    # CL_RemoverItem_carrinho_01,
)
from home_page import (
    CL_HomePage,
    CL_MenuLateral,
    CL_OptnAbout,
    CL_AdicionarItens_Carrinho,
    CL_AcessarCarrinho,
)
from infos_produtos_page import (
    CL_VoltarPara_Produtos,
)
from login_page import (
    CL_LoginValido,
    CL_LoginInvalido,
)
from verificar_elementos import (
    Cl_VerificarElementos_ItensCarrinho
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
        adicionar_itens_carrinho = CL_AdicionarItens_Carrinho(browser)
        voltar_produtos = CL_VoltarPara_Produtos(browser)

        adicionar_itens_carrinho.add_ao_carrinho("Sauce Labs Backpack")
        voltar_produtos.voltar_para_produtos()

        adicionar_itens_carrinho.add_ao_carrinho("Sauce Labs Bike Light")
        voltar_produtos.voltar_para_produtos()

        adicionar_itens_carrinho.add_ao_carrinho("Sauce Labs Onesie")
        voltar_produtos.voltar_para_produtos()


        # 1° Acesso ao carrinho - Página Home
        carrinho = CL_AcessarCarrinho(browser)
        carrinho.entrar_carrinho()



        # 1° Primeira verificação de itns do carrinho - Carrinho

        assert resultado_verificacao_01, "Elementos do carrinho não estão presentes!" #Essa menssagem irá aparecer caso o testde falhar



        #1° Remoção de itens do carrinho - Carrinho
        remover_item = CL_RemoverItens_Carrinho(browser)
        continue_shopping = CL_ContinueShopping(browser)

        remover_item.remover_item_carrinho("Sauce Labs Bike Light")
        remover_item.voltar_pag_anterior()

        remover_item.remover_item_carrinho("Sauce Labs Onesie")
        remover_item.voltar_pag_anterior()
        continue_shopping.continue_shopping_carrinho()


        # 2° Adição de itens ao carrinho - Página Home

        adicionar_itens_carrinho.add_ao_carrinho("Sauce Labs Fleece Jacket")
        adicionar_itens_carrinho.voltar_pag_anterior()

        adicionar_itens_carrinho.add_ao_carrinho("Sauce Labs Bolt T-Shirt")
        voltar_produtos.voltar_para_produtos()


        # 2° Acesso ao carrinho - Página Home
        carrinho = CL_AcessarCarrinho(browser)
        carrinho.entrar_carrinho()
