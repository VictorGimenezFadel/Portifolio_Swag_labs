""""
Métodos reutilizáveis
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def encontrar_elemento(self, locator):
        return self.browser.find_element(*locator)


    def encontrar_elementos(self, locator):
        return self.browser.find_elements(*locator)


    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)


    def clicar(self, locator):
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(locator)).click()


    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não apareceu na tela no tempo esperado"
                                                                # Mensagem para caso o elemento não esteja presente


    def verificar_se_elementos_existem(self, locator): # Usar somente em situações pontuais onde aparecem varios elementos com um mesmo locator
        assert self.encontrar_elementos(locator).is_displayed(), f"Os elementos '{locator}' não aparecem na tela no tempo esperado"


    def voltar_pag_anterior(self):
        self.browser.back()


    def voltar_pag_que_estava(self):
        self.browser.forward()
