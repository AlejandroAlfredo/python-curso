# POO: poliformismo, herencia, encasuplamineto
#lado = 4
#mySquare = Square()
#print(mySquare.lado)
#mySquare.lado = 5
#print(mySquare.lado)
class Square:
    def calcularArea(self, lado):
        resultado = lado ** 2
        return resultado
mySquare = Square()
print(mySquare.calcularArea(4))

