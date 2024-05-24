""""
SEÇÃO 07 - CRIANDO BasePage – PRIMEIROS MÉTODOS GENERICOS
BasePage.py
"""
class CL_BasePage:
    def __init__(self, browser):
        self.browser = browser

    def encontrar_elemento(self, locator):
        return self.browser.find_element(*locator)

    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não apareceu na tela no tempo esperado"
                                                                # Mensagem para caso o elemento não esteja presente
