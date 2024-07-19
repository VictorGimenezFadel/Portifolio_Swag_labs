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
        teclas_numpad = teclas_mapa.get(tecla)
        if teclas_numpad:
            elemento.send_keys(teclas_numpad)
        else:
            raise ValueError(f"Tecla '{tecla}' não é uma tecla do Numpad válida.")


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
        teclas_numericas = teclas_mapa.get(tecla)
        if teclas_numericas:
            elemento.send_keys(teclas_numericas)
        else:
            raise ValueError(f"Tecla '{tecla}' não é uma tecla Numérica válida.")



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
            "Z": "Z",
            "Ç": "Ç",
        }
        teclas_letras = teclas_mapa.get(tecla)
        if teclas_letras:
            elemento.send_keys(teclas_letras)
        else:
            raise ValueError(f"Tecla '{tecla}' não é uma tecla de Letra válida.")



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
            "F12": Keys.F12
        }
        teclas_funcao = teclas_mapa.get(tecla)
        if teclas_funcao:
            elemento.send_keys(teclas_funcao)
        else:
            raise ValueError(f"Tecla '{tecla}' não é uma tecla de Função válida.")



class CL_TeclasMapeadas_Especificas(BasePage):
    def __init__(self, browser):
        self.browser = browser

    def pressionar_tecla_especificas(self, locator, tecla):
        elemento = self.encontrar_elemento(locator)
        teclas_mapa = {
            "HOME": Keys.HOME,
            "END": Keys.END,
            "INSERT": Keys.INSERT,
            "DELETE": Keys.DELETE,
            "BACKSPACE": Keys.BACKSPACE,
            "TAB": Keys.TAB,
            "PgUp": Keys.PAGE_UP,
            "PgDn": Keys.PAGE_DOWN,
            "ENTER": Keys.ENTER,
            "ESPAÇO": Keys.SPACE,
            "SHIFT": Keys.SHIFT,
            "CTRL": Keys.CONTROL,
            "LEFT_ALT": Keys.LEFT_ALT,
            "ESC": Keys.ESCAPE,
            "PAUSE": Keys.PAUSE,
            "ARROW_UP": Keys.ARROW_UP,
            "ARROW_DOWN": Keys.ARROW_DOWN,
            "ARROW_LEFT": Keys.ARROW_LEFT,
            "ARROW_RIGHT": Keys.ARROW_RIGHT,
        }
        teclas_especificas = teclas_mapa.get(tecla)
        if teclas_especificas:
            elemento.send_keys(teclas_especificas)
        else:
            raise ValueError(f"Tecla '{tecla}' não é uma tecla Especifica válida.")



class CL_TeclasMapeadas_AtalhosTecla(BasePage): # Mapear os demais atalhos de acordo com a necessidade
    def __init__(self, browser):
        self.browser = browser

    def pressionar_atalho_teclas(self, locator, tecla):
        elemento = self.encontrar_elemento(locator)
        teclas_mapa = {
            ("Ctrl", "C"): "copied_text",   # Copiar texto
            ("Ctrl", "V"): "pasted_text",   # Colar texto
        }
        atalho_teclas = teclas_mapa.get(tecla)
        if atalho_teclas:
            elemento.send_keys(atalho_teclas)
        else:
            raise ValueError(f"Tecla '{tecla}' não é uma tecla de Letra válida.")
