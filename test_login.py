"""
Navegação básica no site Swag Labs - Interações dentro da tela de login

Esse teste está em desenvolvimento
"""
# Import dos arquivos .py e das classes presentes dentro deles
import pytest
from conftest import browser
from login_page import (
    CL_LoginValido,
    CL_LoginInvalido,
)


@pytest.mark.usefixtures("browser")
@pytest.mark.login  # mark para executar o teste através do pytest
class TestCT01_SwagLabs_login:
    def test_ct01_swaglabs_login(self, browser):
        # Tela de login

        # Primeiro Login - Inválido
        login_invalido = CL_LoginInvalido(browser)
        login_invalido.fazer_login_invalido("standard_user", "senha_errada")

        login_invalido.verificar_mensagem_de_erro_login()
        login_invalido.recarregar_pagina()



        # Primeiro Login - Válido
        login_valido = CL_LoginValido(browser)
        login_valido.fazer_login("standard_user", "secret_sauce")
