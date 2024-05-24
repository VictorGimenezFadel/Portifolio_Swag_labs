"""
Navegação básica no site Swag Labs

Teste com time.sleep para que possa ser visualizado as execuções de forma mais clara, para ver todas as interações, como se o site estivesse sendo
acessado por uma pessoa mesmo
"""

"""
Navegação básica no site Swag Labs

Esse teste está em desenvolvimento
"""
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.login_page import LoginPage
from conftest import browser


@pytest.mark.usefixtures("browser")
@pytest.mark.login
class TestCT01_Swag_labs:
    def test_swag_labs_navegação(self, browser):

        login_page = LoginPage(browser)
        login_page.fazer_login("standard_user", "secret_sauce")


        #Tela inicial - Home

        #Primeira interação com o Menu lateral (3 risquinhos)
        menu_lateral_esq = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_lateral_esq.click()
        time.sleep(1)



        #Opção About (Sobre)
        optn_about = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='about_sidebar_link']")))
        optn_about.click()
        time.sleep(1)



        #Pop-up canto esquerdo
        wait = WebDriverWait(browser, 30) #Timeout para esperar que todos os itens da página sejam carregados em até 30 segundos, até que seja possivel interajir com o pop-up
        pop_up = wait.until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))) #Verifica se o pop-up está visivel e pode ser clicavel

        #Fechar pop-up
        fechar_pop_up = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='onetrust-accept-btn-handler']")))
        fechar_pop_up.click()
        time.sleep(1)



        #Voltar para a tela anterior -Home (Back)
        browser.back()
        time.sleep(1)





        #Interação com o carrinho (ADD)

        #Adicionar item ao carrinho (Sauce Labs Backpack)
        add_carrinho_backpack = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        add_carrinho_backpack.click()
        time.sleep(1)



        #Adicionar item ao carrinho (Sauce Labs Bike Light)
        add_carrinho_bike_light = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
        add_carrinho_bike_light.click()
        time.sleep(1)



        #Adicionar item ao carrinho (Sauce Labs Onesie)
        browser.execute_script("window.scrollBy(0, 500);") #Rolar tela para baixo
        add_carrinho_onesie = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
        time.sleep(1)
        add_carrinho_onesie.click()
        time.sleep(1)



        #Rolar toda tela para cima
        browser.execute_script("window.scrollBy(0, -500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))) #Espera até que o elemento desejado seja visível e clicavel na página
        time.sleep(1)





        #Dentro do carrinho - icone

        #Entrar no carrinho
        entrar_carrinho = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
        entrar_carrinho.click()
        time.sleep(1)



        #Remover item do carrinho (Bike)
        remover_item_bike = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-bike-light")))
        remover_item_bike.click()
        time.sleep(1)



        #Remover item do carrinho (Onesie)
        remover_item_onesie = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-onesie")))
        remover_item_onesie.click()
        time.sleep(1)



        #Voltar para a tela anterior - Home(Back)
        browser.back()
        time.sleep(1)



        #Adicionar item ao carrinho (Sauce Labs Fleece Jacket)
        add_carrinho_fleece_jacket = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))) #Espera até que o elemento desejado seja visível na página
        browser.execute_script("window.scrollBy(0, 200);")
        time.sleep(1)
        add_carrinho_fleece_jacket.click()
        time.sleep(1)



        #Adicionar item ao carrinho (Sauce Labs Bolt T-Shirt)
        add_carrinho_bolt_tshirt = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        add_carrinho_bolt_tshirt.click()
        time.sleep(1)



        #Rolar toda para cima
        browser.execute_script("window.scrollBy(0, -500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))) #Espera até que o elemento desejado seja visível na página
        time.sleep(1)



        #Entrar no carrinho
        entrar_carrinho = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
        entrar_carrinho.click()
        time.sleep(1)



        #Rolar toda para baixo
        browser.execute_script("window.scrollBy(0, 500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "checkout"))) #Espera até que o elemento desejado seja visível na página
        time.sleep(1)



        #Realizar checkout
        btn_checkout = browser.find_element(By.ID, "checkout")
        btn_checkout.click()
        time.sleep(1)





        #Rolar toda tela para cima
        browser.execute_script("window.scrollBy(0, -500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "first-name"))) #Espera até que o elemento desejado seja visível e clicavel na página
        time.sleep(1)



        #Checkout

        #Primeiro nome (Firt name)
        first_name = browser.find_element(By.ID, "first-name")
        first_name.send_keys("Victor Gimenez Fadel")
        time.sleep(1)



        #Apelido (Last name)
        last_name = browser.find_element(By.ID, "last-name")
        last_name.send_keys("Victor")
        time.sleep(1)



        #CEP (Zip/Postal Code)
        postal_code = browser.find_element(By.ID, "postal-code")
        postal_code.send_keys("12345678")
        time.sleep(1)



        #Rolar toda tela para baixo
        browser.execute_script("window.scrollBy(0, 500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "continue"))) #Espera até que o elemento desejado seja visível e clicavel na página
        time.sleep(1)



        #Finalizar checkout (Continue)
        btn_continue = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "continue")))
        btn_continue.click()
        time.sleep(1)



        #Finalizar compra (Finish)
        btn_finish =WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "finish")))
        btn_finish.click()
        time.sleep(1)



        #Voltar para a página inicial (Back Home)
        btn_back_home = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID,"back-to-products")))
        btn_back_home.click()
        time.sleep(1)





        #Interação com o filtro

        #filtro
        filtro = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@class='product_sort_container']")))
        filtro.click()
        time.sleep(2)



        #Opção de Z a A
        optn_z_a = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//option[@value='za']")))
        optn_z_a.click()
        time.sleep(1)



        #Segunda interação com o Menu lateral (3 risquinhos)
        menu_lateral_esq = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_lateral_esq.click()
        time.sleep(1)



        #Opção About (Sobre)
        optn_about = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable(By.XPATH, "//a[@id='about_sidebar_link']"))
        optn_about.click()
        time.sleep(1)



        time.sleep(2)
        quit()
      
