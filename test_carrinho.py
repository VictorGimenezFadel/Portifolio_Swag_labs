"""
Navegação básica no site Swag Labs - Interações dentro do carrinho

Esse teste está em desenvolvimento
"""
# Import dos arquivos .py e das classes presentes dentro deles
import pytest
from conftest import browser
from carrinho_page import (
    CL_RemoverItens_Carrinho,
    CL_ContinueShopping,
    CL_RealizarCheckout,
)
from home_page import (
    CL_HomePage,
    CL_AdicionarItens_Carrinho,
    CL_AcessarCarrinho,
)
from infos_produtos_page import (
    CL_VoltarPara_Produtos,
)
from login_page import (
    CL_LoginValido,
)
from verificar_elementos import (
    Cl_VerificarElementos_ItensCarrinho
)


@pytest.mark.usefixtures("browser")
@pytest.mark.about  # mark para executar o teste através do pytest
class TestCT04_SwagLabs_about:
    def test_ct04_swaglabs_carrinho(self, browser):
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
