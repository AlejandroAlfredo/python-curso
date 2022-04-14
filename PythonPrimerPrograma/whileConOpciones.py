#ciclo while que tenga la opcion de continuar o salir
x = 1
valueOne = int(input("Escribe el limite de las impresiones: "))
while x <= valueOne:
    print(x)
    if(x == 5):
        options = int(input("Deseas continuar o salir? \n1.Continuar 2.Salir"))
        if(options == 2):
            exit()
        elif(options == 1):
            x = x + 1
            continue
    x = x + 1