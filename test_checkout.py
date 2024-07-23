"""
Navegação básica no site Swag Labs - Interações dentro do carrinho para realizar o checkout dos produtos

Esse teste está em desenvolvimento
"""
# Import dos arquivos .py e das classes presentes dentro deles
import pytest
from conftest import browser
from Pages.carrinho_page import (
    CL_RemoverItens_Carrinho,
    CL_ContinueShopping,
    CL_RealizarCheckout,
)
from Pages.checkout_page import (
    CL_InfosCheckout,
    CL_ContinueCheckout,
    CL_FinalizarCheckout,
    CL_Voltar_PagInicial,
)
from Pages.home_page import (
    CL_HomePage,
    CL_AdicionarItens_Carrinho,
    CL_AcessarCarrinho,
)
from Pages.infos_produtos_page import (
    CL_VoltarPara_Produtos,
)
from Pages.login_page import (
    CL_LoginValido,
)
from GlobalFeatures.verificar_elementos import (
    Cl_VerificarElementos_ItensCarrinho
)


@pytest.mark.usefixtures("browser")
@pytest.mark.checkout  # mark para executar o teste através do pytest
class TestCT05_SwagLabs_checkout:
    def test_ct05_swaglabs_checkout(self, browser):
        # Tela de login

        # Login
        login_valido = CL_LoginValido(browser)
        login_valido.fazer_login("standard_user", "secret_sauce")



        # Tela inicial - Home

        # Conexão com a home_page.py e os métodos dentro dela - Home Page
        home_page = CL_HomePage(browser)  # CL_LoginPage é a class la no arquivo login_page.py
        home_page.verificar_login_bem_sucedido()



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
        acessar_carrinho = CL_AcessarCarrinho(browser)
        acessar_carrinho.entrar_carrinho()



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



        # 1° Verificação de itns do carrinho - Carrinho
        verificar_produto = Cl_VerificarElementos_ItensCarrinho(browser)

        verificar_produto.verificar_itens_presentes("Sauce Labs Backpack")
        verificar_produto.verificar_itens_presentes("Sauce Labs Fleece Jacket")
        verificar_produto.verificar_itens_presentes("Sauce Labs Bolt T-Shirt")



        # 1° Interação com o botão Checkout - Carrinho
        realizar_checkout = CL_RealizarCheckout(browser)
        realizar_checkout.realizar_checkout_carrinho()



        # 1° Continue Checkout - Checkout
        infos_checkout = CL_InfosCheckout(browser)
        btn_continue_checkout = CL_ContinueCheckout(browser)
        btn_finish_checkout = CL_FinalizarCheckout(browser)
        btn_back_home = CL_Voltar_PagInicial(browser)

        infos_checkout.inserir_infos("Victor", "Gimenez", "12345-678")
        btn_continue_checkout.continuar_checkout()
        btn_finish_checkout.finalizar_checkout()
        btn_back_home.voltar_pagina_incial()
