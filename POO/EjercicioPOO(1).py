# 1. Pedir N palabras, inprimir 2 lineas, en la primera el numero de palabras distintas,
# en la segunda cuantas veces se repiten de acuerdo al orden.
# Ejemplo: jesus   | # primera linea: 3
#          juan    | # segunda linea: 2*jesus 1*juan 1*pedro
#          pedro   |
#          jesus   |
class Solution:
    def myLine(self, value):
        self.n = len(list)
        self.var = list.count(value)
        dict[value] = self.var
        self.myFormat = "{} palabras\n{}"
        print(self.myFormat.format(self.n, dict))

class Palabras:
    def __init__(self):
        value = input("Escribe una palabra: ")
        list.append(value)
        mySolution = Solution()
        mySolution.myLine(value)
        myPalabras = Palabras()

dict = {}
value = ""
list = []
myPalabras = Palabras()