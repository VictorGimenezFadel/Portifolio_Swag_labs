""""
Arquivo destinado para o mepeamento de todas as teclas do teclado fisico

Esse método é somete para ilustrar o que o método deve fazer, pois não apliquei no arquivo do teste
"""""
from base_page import BasePage
from conftest import browser
from selenium.webdriver import Keys


class CL_TeclasMapeadas_Numpad(BasePage):
    def __init__(self, browser):
        self.browser = browser

    def pressionar_tecla_numpad(self, locator, tecla):
        elemento = self.encontrar_elemento(locator)
        teclas_mapa = {
            "NUMBER0": Keys.NUMPAD0,
            "NUMBER1": Keys.NUMPAD1,
            "NUMBER2": Keys.NUMPAD2,
            "NUMBER3": Keys.NUMPAD3,
            "NUMBER4": Keys.NUMPAD4,
            "NUMBER5": Keys.NUMPAD5,
            "NUMBER6": Keys.NUMPAD6,
            "NUMBER7": Keys.NUMPAD7,
            "NUMBER8": Keys.NUMPAD8,
            "NUMBER9": Keys.NUMPAD9
        }
        elemento.send_keys(teclas_mapa.get(tecla))



class CL_TeclasMapeadas_Numerica(BasePage):
    def __init__(self, browser):
            self.browser = browser

    def pressionar_tecla_numerica(self, locator, tecla):
        elemento = self.encontrar_elemento(locator)
        teclas_mapa = {
            "TECLA1": "1",
            "TECLA2": "2",
            "TECLA3": "3",
            "TECLA4": "4",
            "TECLA5": "5",
            "TECLA6": "6",
            "TECLA7": "7",
            "TECLA8": "8",
            "TECLA9": "9",
            "TECLA0": "0"
        }
        elemento.send_keys(teclas_mapa.get(tecla))



class CL_TeclasMapeadas_Letra(BasePage):
    def __init__(self, browser):
        self.browser = browser

    def pressionar_tecla_letra(self, locator, tecla):
        elemento = self.encontrar_elemento(locator)
        teclas_mapa = {
            "A": "A",
            "B": "B",
            "C": "C",
            "D": "D",
            "E": "E",
            "F": "F",
            "G": "G",
            "H": "H",
            "I": "I",
            "J": "J",
            "K": "K",
            "L": "L",
            "M": "M",
            "N": "N",
            "O": "O",
            "P": "P",
            "Q": "Q",
            "R": "R",
            "S": "S",
            "T": "T",
            "U": "U",
            "V": "V",
            "W": "W",
            "X": "X",
            "Y": "Y",
            "Z": "Z"
        }
        elemento.send_keys(teclas_mapa[tecla])



class CL_TeclasMapeadas_Funcao(BasePage):
    def __init__(self, browser):
        self.browser = browser

    def pressionar_tecla_funcao(self, locator, tecla):
        elemento = self.encontrar_elemento(locator)
        teclas_mapa = {
            "F1": Keys.F1,
            "F2": Keys.F2,
            "F3": Keys.F3,
            "F4": Keys.F4,
            "F5": Keys.F5,
            "F6": Keys.F6,
            "F7": Keys.F7,
            "F8": Keys.F8,
            "F9": Keys.F9,
            "F10": Keys.F10,
            "F11": Keys.F11,
            "F12": Keys.F12,
        }



class CL_TeclasMapeadas_Especificas(BasePage):
    def __init__(self, browser):
        self.browser = browser

    def pressionar_tecla_especificas(self, locator, tecla):
        elemento = self.encontrar_elemento(locator)
        if tecla == "HOME":
            elemento.send_keys(Keys.HOME)
        elif tecla == "END":
            elemento.send_keys(Keys.END)
        elif tecla == "INSERT":
            elemento.send_keys(Keys.INSERT)
        elif tecla == "DELETE":
            elemento.send_keys(Keys.DELETE)
        elif tecla == "BACKSPACE":
            elemento.send_keys(Keys.BACKSPACE)
        elif tecla == "TAB":
            elemento.send_keys(Keys.TAB)
        # elif tecla == "":
        #     elemento.send_keys(Keys.)
        # elif tecla == "":
        #     elemento.send_keys(Keys.)
        # elif tecla == "":
        #     elemento.send_keys(Keys.)




        elif tecla == "ENTER":
            elemento.send_keys(Keys.ENTER)
        elif tecla == "ESPAÇO":
            elemento.send_keys(Keys.SPACE)
        elif tecla == "SHIFT":
            elemento.send_keys(Keys.SHIFT)
        elif tecla == "CTRL":
            elemento.send_keys(Keys.CONTROL)
        elif tecla == "LEFT_ALT":
            elemento.send_keys(Keys.LEFT_ALT)

