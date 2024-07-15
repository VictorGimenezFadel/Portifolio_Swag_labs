"""
Navegação básica no site Swag Labs - Interações página incial

Esse teste está em desenvolvimento
"""
# Import dos arquivos .py e das classes presentes dentro deles
import pytest
from conftest import browser
from home_page import (
    CL_HomePage,
    CL_AdicionarItens_Carrinho,
)
from infos_produtos_page import (
    CL_VoltarPara_Produtos,
)
from login_page import (
    CL_LoginValido,
)


@pytest.mark.usefixtures("browser")
@pytest.mark.navegar # mark para executar o teste através do pytest


class TestCT01_Swag_labs:
    def test_ct01_swaglabs_navegação(self, browser):

        # Tela de login

        # Primeiro Login - Válido
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

        adicionar_itens_carrinho.add_ao_carrinho("Sauce Labs Fleece Jacket")
        adicionar_itens_carrinho.voltar_pag_anterior()

        adicionar_itens_carrinho.add_ao_carrinho("Sauce Labs Bolt T-Shirt")
        voltar_produtos.voltar_para_produtos()
