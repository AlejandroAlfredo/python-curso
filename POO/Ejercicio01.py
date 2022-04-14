# 1.pedir y crear 2 listas, y que elimine de la primera lista los elementos que vengan en la segunda lista.
class Estructura:
    def __init__(self):
        print("\n-- Inicio --")
        self.valueOne = input("Escribe algo(Escribe exit para salir): ")
        if(self.valueOne == "exit"):
            Estructura.Proceso(self)
        else:
            listOne.append(self.valueOne)

        print(listOne)
        Estructura()

    def Proceso(self):
        print("\n-- Eliminacion --")
        self.value = input("Eliminar(Escribe exit para salir): ")
        if(self.value == "exit"):
            Estructura.Eliminacion(self)
        else:
            listTwo.append(self.value)

        print(listTwo)
        Estructura.Proceso(self)

    def Eliminacion(self):
        for self.x in listTwo:
            if(self.x in listOne):
                listOne.remove(self.x)
        print("Resultado de la nueva lista:")
        print(listOne)
        Estructura()

listOne = []
listTwo = []
myEstructura = Estructura()