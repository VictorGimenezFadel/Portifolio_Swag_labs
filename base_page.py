""""
Métodos reutilizáveis
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage():
    def __init__(self, browser):
        self.browser = browser


    def encontrar_elemento(self, locator):
        return self.browser.find_element(*locator)



    def encontrar_elementos(self, locator):
        return self.browser.find_elements(*locator)



    def verificar_se_elemento_existe(self, locator):
        self.esperar_elemento_aparecer(locator)
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não está presente"
                                                                # Mensagem para caso o elemento não esteja presente



    def verificar_se_elementos_existem(self, locator): # Usar somente em situações pontuais onde aparecem varios elementos com um mesmo locator
        self.esperar_elemento_aparecer(locator)
        assert self.encontrar_elementos(locator).is_displayed(), f"Os elementos '{locator}' não aparecem na tela no tempo esperado"



    def pegar_texto_elemento (self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text



    def esperar_elemento_aparecer(self, locator):
        return WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(*locator))



    def verificar_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator), f"Elemento '{locator}' não existe, mas é esperado que exista"
                                                    # Essa mensagem irá aparecer quando a verificação der erro



    def verificar_elemento_nao_existe(self, locator):
        assert len(self.encontrar_elementos(locator)) == 0, f"Elemento '{locator}' existe, mas é esperado que não exista"
                                                    # Essa mensagem irá aparecer quando a verificação der erro



    def clicar(self, locator):
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(locator)).click()



    def clique_duplo(self, locator):
        elemento = self.esperar_elemento_aparecer(locator)
        ActionChains(self.browser).double_click(elemento).perform()



    def clique_btn_direito(self, locator):
        elemento = self.esperar_elemento_aparecer(locator)
        ActionChains(self.browser).context_click(elemento).perform()



    # Esse método é somete para ilustrar o que o método deve fazer, pois não apliquei no arquivo do teste
    def pressionar_tecla_especifica(self, locator, key):
        elemento = self.encontrar_elemento(locator)
        if key == "ENTER":
            elemento.send_keys(Keys.ENTER)
        elif key == "ESPAÇO":
            elemento.send_keys(Keys.SPACE)
        elif key == "SHIFT":
            elemento.send_keys(Keys.SHIFT)
        elif key == "CTRL":
            elemento.send_keys(Keys.CONTROL)
        elif key == "LEFT_ALT":
            elemento.send_keys(Keys.LEFT_ALT)



    def pressionar_tecla_letra(self, locator, key):
        elemento = self.encontrar_elemento(locator)
        if key == "A":
            elemento.send_keys("A")
        elif key == "B":
            elemento.send_keys("B")
        elif key == "C":
            elemento.send_keys("C")
        elif key == "D":
            elemento.send_keys("D")
        elif key == "E":
            elemento.send_keys("E")



    def pressionar_tecla_numero(self, locator, key):
        elemento = self.encontrar_elemento(locator)
        if key == "1":
            elemento.send_keys("1")
        elif key == "2":
            elemento.send_keys("2")
        elif key == "3":
            elemento.send_keys("3")
        elif key == "4":
            elemento.send_keys("4")
        elif key == "5":
            elemento.send_keys("5")



    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)



    def recarregar_pagina(self):
        self.browser.refresh()



    def voltar_pag_anterior(self):
        self.browser.back()



    def voltar_pag_que_estava(self):
        self.browser.forward()
