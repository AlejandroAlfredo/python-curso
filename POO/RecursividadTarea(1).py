# 1.Pedir una cantidad e indicar cuantas monedas dar de cambio.
# monedas 1, 2, 5, 10. se debe iniciar con la mayor(la de 10) y terminar con la menor(1)
class Operations:
    def calucular(self, data):
        self.data = data
        for x in list:
            self.resultado = self.data / x
            self.resultado = int(self.resultado)
            self.myFormat = "se usaron {} de ${}"
            self.data = self.data % x
            print(self.myFormat.format(self.resultado, x))

class Proceso:
    def __init__(self):
        data = int(input("Escribe una cantidad de dinero: $"))
        myOperations = Operations()
        myOperations.calucular(data)
        myProceso = Proceso()

data = 0
list = [10,5,2,1]
myProceso = Proceso()