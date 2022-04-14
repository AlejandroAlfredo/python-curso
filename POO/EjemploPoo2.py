# EJEMPLO DE POO
class Figure:
    def cuadrado(self, lado):
        resultado = lado ** 2
        myFormat = "El area del cuadrado es {}"
        cuadrado = myFormat.format(resultado)
        return cuadrado
    def triangulo(self, base, altura):
        resultado = (base * altura) / 2
        myFormat = "El area del triangulo es {}"
        triangulo = myFormat.format(resultado)
        return triangulo
    def circulo(self, radio):
        PI = 3.1416
        resultado = (PI * radio**2)
        myFormat = "El area del circulo es {:.2f}"
        circulo = myFormat.format(resultado)
        return circulo
myFigure = Figure()
print(myFigure.cuadrado(4))
print(myFigure.triangulo(8,5))
print(myFigure.circulo(8))