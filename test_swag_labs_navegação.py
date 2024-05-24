"""
Navegação básica no site Swag Labs

Arquivo central onde os médotos e funções serão aplicados

Esse teste está em desenvolvimento
"""
import time
import pytest
from Pages.login_page import CL_LoginPage  # Pages é a pasta onde está a login_page
from Pages.home_page import CL_HomePage, CL_MenuLateral  # Pages é a pasta onde está a home_page

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser


@pytest.mark.usefixtures("browser")
@pytest.mark.navegar #mark para executar o teste através do pytest
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






        #Opção About (Sobre)
        optn_about = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='about_sidebar_link']")))
        optn_about.click()



        #Pop-up canto esquerdo
        wait = WebDriverWait(browser, 30) #Timeout para esperar que todos os itens da página sejam carregados em até 30 segundos, até que seja possivel interajir com o pop-up
        pop_up = wait.until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))) #Verifica se o pop-up está visivel e pode ser clicavel

        #Fechar pop-up
        fechar_pop_up = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='onetrust-accept-btn-handler']")))
        fechar_pop_up.click()



        #Voltar para a tela anterior -Home (Back)
        browser.back()





        #Interação com o carrinho (ADD)

        #Adicionar item ao carrinho (Sauce Labs Backpack)
        add_carrinho_backpack = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        add_carrinho_backpack.click()



        #Adicionar item ao carrinho (Sauce Labs Bike Light)
        add_carrinho_bike_light = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
        add_carrinho_bike_light.click()



        #Adicionar item ao carrinho (Sauce Labs Onesie)
        browser.execute_script("window.scrollBy(0, 500);") #Rolar tela para baixo
        add_carrinho_onesie = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
        add_carrinho_onesie.click()



        #Rolar toda tela para cima
        browser.execute_script("window.scrollBy(0, -500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))) #Espera até que o elemento desejado seja visível e clicavel na página





        #Dentro do carrinho - icone

        #Entrar no carrinho
        entrar_carrinho = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
        entrar_carrinho.click()



        #Remover item do carrinho (Bike)
        remover_item_bike = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-bike-light")))
        remover_item_bike.click()



        #Remover item do carrinho (Onesie)
        remover_item_onesie = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-onesie")))
        remover_item_onesie.click()



        #Voltar para a tela anterior - Home(Back)
        browser.back()



        #Adicionar item ao carrinho (Sauce Labs Fleece Jacket)
        add_carrinho_fleece_jacket = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))) #Espera até que o elemento desejado seja visível na página
        browser.execute_script("window.scrollBy(0, 200);")
        add_carrinho_fleece_jacket.click()



        #Adicionar item ao carrinho (Sauce Labs Bolt T-Shirt)
        add_carrinho_bolt_tshirt = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        add_carrinho_bolt_tshirt.click()



        #Rolar toda para cima
        browser.execute_script("window.scrollBy(0, -500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))) #Espera até que o elemento desejado seja visível na página



        #Entrar no carrinho
        entrar_carrinho = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
        entrar_carrinho.click()



        #Rolar toda para baixo
        browser.execute_script("window.scrollBy(0, 500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "checkout"))) #Espera até que o elemento desejado seja visível na página



        #Realizar checkout
        btn_checkout = browser.find_element(By.ID, "checkout")
        btn_checkout.click()





        #Rolar toda tela para cima
        browser.execute_script("window.scrollBy(0, -500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "first-name"))) #Espera até que o elemento desejado seja visível e clicavel na página



        #Checkout

        #Primeiro nome (Firt name)
        first_name = browser.find_element(By.ID, "first-name")
        first_name.send_keys("Victor Gimenez Fadel")



        #Apelido (Last name)
        last_name = browser.find_element(By.ID, "last-name")
        last_name.send_keys("Victor")



        #CEP (Zip/Postal Code)
        postal_code = browser.find_element(By.ID, "postal-code")
        postal_code.send_keys("12345678")



        #Rolar toda tela para baixo
        browser.execute_script("window.scrollBy(0, 500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "continue"))) #Espera até que o elemento desejado seja visível e clicavel na página



        #Finalizar checkout (Continue)
        btn_continue = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "continue")))
        btn_continue.click()



        #Finalizar compra (Finish)
        btn_finish =WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "finish")))
        btn_finish.click()



        #Voltar para a página inicial (Back Home)
        btn_back_home = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID,"back-to-products")))
        btn_back_home.click()





        #Interação com o filtro

        #filtro
        filtro = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@class='product_sort_container']")))
        filtro.click()



        #Opção de Z a A
        optn_z_a = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//option[@value='za']")))
        optn_z_a.click()



        #Segunda interação com o Menu lateral (3 risquinhos)
        menu_lateral_esq = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_lateral_esq.click()



        #Opção About (Sobre)
        optn_about = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable(By.XPATH, "//a[@id='about_sidebar_link']"))
        optn_about.click()



        time.sleep(2)
        quit()
