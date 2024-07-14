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
        elif key == "6":
            elemento.send_keys("6")
        elif key == "7":
            elemento.send_keys("7")
        elif key == "8":
            elemento.send_keys("8")
        elif key == "9":
            elemento.send_keys("9")
        elif key == "0":
            elemento.send_keys("0")



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
        elif key == "F":
            elemento.send_keys("F")
        elif key == "G":
            elemento.send_keys("G")
        elif key == "H":
            elemento.send_keys("H")
        elif key == "I":
            elemento.send_keys("I")
        elif key == "J":
            elemento.send_keys("J")
        elif key == "K":
            elemento.send_keys("K")
        elif key == "L":
            elemento.send_keys("L")
        elif key == "M":
            elemento.send_keys("M")
        elif key == "N":
            elemento.send_keys("N")
        elif key == "O":
            elemento.send_keys("O")
        elif key == "P":
            elemento.send_keys("P")
        elif key == "Q":
            elemento.send_keys("Q")
        elif key == "R":
            elemento.send_keys("R")
        elif key == "S":
            elemento.send_keys("S")
        elif key == "T":
            elemento.send_keys("T")
        elif key == "U":
            elemento.send_keys("U")
        elif key == "V":
            elemento.send_keys("V")
        elif key == "W":
            elemento.send_keys("W")
        elif key == "X":
            elemento.send_keys("X")
        elif key == "Y":
            elemento.send_keys("Y")
        elif key == "Z":
            elemento.send_keys("Z")



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
