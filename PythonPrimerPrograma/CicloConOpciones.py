#ciclo y llegando al 5 preguntar si quieres continuar o salir y cumplir respectivas funciones
x = 0
valueOne = int(input("Escribe el limite de impresiones: "))
for x in range (valueOne):
    print(x)
    if(x == 5):
        valueTwo = int(input("Desea continuar o salir? \n1.Continuar 2.Salir"))
        if(valueTwo == 1):
            continue
        if(valueTwo == 2):
            exit()