""""
Arquivo destinado para o mepeamento de todas as teclas do teclado fisico

Esse método é somete para ilustrar o que o método deve fazer, pois não apliquei no arquivo do teste
"""""
from base_page import BasePage
from conftest import browser
from selenium.webdriver import Keys


class CL_TeclasMapeadas(BasePage):
    def __init__(self, browser):
        self.browser = browser

    

    def pressionar_tecla_numeros(self, locator, tecla):
        elemento = self.encontrar_elemento(locator)
        if tecla == "NUMBER0":
            elemento.send_keys(Keys.NUMPAD0)
        elif tecla == "NUMBER1":
            elemento.send_keys(Keys.NUMPAD1)
        elif tecla == "NUMBER2":
            elemento.send_keys(Keys.NUMPAD2)
        elif tecla == "NUMBER3":
            elemento.send_keys(Keys.NUMPAD3)
        elif tecla == "NUMBER4":
            elemento.send_keys(Keys.NUMPAD4)
        elif tecla == "NUMBER5":
            elemento.send_keys(Keys.NUMPAD5)
        elif tecla == "NUMBER6":
            elemento.send_keys(Keys.NUMPAD6)
        elif tecla == "NUMBER7":
            elemento.send_keys(Keys.NUMPAD7)
        elif tecla == "NUMBER8":
            elemento.send_keys(Keys.NUMPAD8)
        elif tecla == "NUMBER9":
            elemento.send_keys(Keys.NUMPAD9)
        elif tecla == "TECLA1":
            elemento.send_keys("1")
        elif tecla == "TECLA2":
            elemento.send_keys("2")
        elif tecla == "TECLA3":
            elemento.send_keys("3")
        elif tecla == "TECLA4":
            elemento.send_keys("4")
        elif tecla == "TECLA5":
            elemento.send_keys("5")
        elif tecla == "TECLA6":
            elemento.send_keys("6")
        elif tecla == "TECLA7":
            elemento.send_keys("7")
        elif tecla == "TECLA8":
            elemento.send_keys("8")
        elif tecla == "TECLA9":
            elemento.send_keys("9")
        elif tecla == "TECLA0":
            elemento.send_keys("0")



    def pressionar_tecla_letra(self, locator, tecla):
        elemento = self.encontrar_elemento(locator)
        if tecla == "A":
            elemento.send_keys("A")
        elif tecla == "B":
            elemento.send_keys("B")
        elif tecla == "C":
            elemento.send_keys("C")
        elif tecla == "D":
            elemento.send_keys("D")
        elif tecla == "E":
            elemento.send_keys("E")
        elif tecla == "F":
            elemento.send_keys("F")
        elif tecla == "G":
            elemento.send_keys("G")
        elif tecla == "H":
            elemento.send_keys("H")
        elif tecla == "I":
            elemento.send_keys("I")
        elif tecla == "J":
            elemento.send_keys("J")
        elif tecla == "K":
            elemento.send_keys("K")
        elif tecla == "L":
            elemento.send_keys("L")
        elif tecla == "M":
            elemento.send_keys("M")
        elif tecla == "N":
            elemento.send_keys("N")
        elif tecla == "O":
            elemento.send_keys("O")
        elif tecla == "P":
            elemento.send_keys("P")
        elif tecla == "Q":
            elemento.send_keys("Q")
        elif tecla == "R":
            elemento.send_keys("R")
        elif tecla == "S":
            elemento.send_keys("S")
        elif tecla == "T":
            elemento.send_keys("T")
        elif tecla == "U":
            elemento.send_keys("U")
        elif tecla == "V":
            elemento.send_keys("V")
        elif tecla == "W":
            elemento.send_keys("W")
        elif tecla == "X":
            elemento.send_keys("X")
        elif tecla == "Y":
            elemento.send_keys("Y")
        elif tecla == "Z":
            elemento.send_keys("Z")



    def pressionar_tecla_funcao(self, locator, tecla):
        elemento = self.encontrar_elemento(locator)
        if tecla == "F1":
            elemento.send_keys(Keys.F1)
        elif tecla == "F2":
            elemento.send_keys(Keys.F2)
        elif tecla == "F3":
            elemento.send_keys(Keys.F3)
        elif tecla == "F4":
            elemento.send_keys(Keys.F4)
        elif tecla == "F5":
            elemento.send_keys(Keys.F5)
        elif tecla == "F6":
            elemento.send_keys(Keys.F6)
        elif tecla == "F7":
            elemento.send_keys(Keys.F7)
        elif tecla == "F8":
            elemento.send_keys(Keys.F8)
        elif tecla == "F9":
            elemento.send_keys(Keys.F9)
        elif tecla == "F10":
            elemento.send_keys(Keys.F10)
        elif tecla == "F11":
            elemento.send_keys(Keys.F11)
        elif tecla == "F12":
            elemento.send_keys(Keys.F12)


    
    def pressionar_tecla_especificas(self, locator, tecla):
        elemento = self.encontrar_elemento(locator)
        if tecla == "HOME":
            elemento.send_keys(Keys.HOME)
        elif tecla == "END"
            elemento.send_keys(Keys.END)
        elif tecla == "INSERT"
            elemento.send_keys(Keys.INSERT)
        elif tecla == "DELETE":
            elemento.send_keys(Keys.DELETE)
        elif tecla == "BACKSPACE"
            elemento.send_keys(Keys.BACKSPACE)
        elif tecla == "TAB"
            elemento.send_keys(Keys.TAB)
        elif tecla == ""
            elemento.send_keys(Keys.)
        elif tecla == ""
            elemento.send_keys(Keys.)
        elif tecla == ""
            elemento.send_keys(Keys.)




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
