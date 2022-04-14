# Realizar un programa para calculo de area de figura geometricas:
# menu
# cuadrado, rectangulo, triangulo, pentagono, hexagono, 6.salir
# funciones o metodos
def myHexagono():
    try:
        print("-- Eligio hexagono --")
        p = float(input("Escribe el valor del perimetro: "))
        a = float(input("Escribe el valor del apotema: "))
        area = (p * a) / 2
        myFormat = "El area del hexagono es: {}"
        print(myFormat.format(area))
    except:
        print("\n--> solo puedes escribir numeros, ahora volvera al menu principal. <--\n")

def myPentagono():
    try:
        print("-- Eligio pentagono --")
        p = float(input("Escribe el valor del perimetro: "))
        a = float(input("Escribe el valor del apotema: "))
        area = (p * a) / 2
        myFormat = "El area del pentagono es: {}"
        print(myFormat.format(area))
    except:
        print("\n--> solo puedes escribir numeros, ahora volvera al menu principal. <--\n")

def myTriangulo():
    try:
        print("-- Eligio triangulo --")
        b = float(input("Escribe el valor de la base: "))
        h = float(input("Escribe el valor de la altura: "))
        a = (b * h) / 2
        myFormat = "El area del triangulo es: {}"
        print(myFormat.format(a))
    except:
        print("\n--> solo puedes escribir numeros, ahora volvera al menu principal. <--\n")

def myRectangulo():
    try:
        print("-- Eligio rectangulo --")
        b = float(input("Escribe el valor de la base: "))
        h = float(input("Escribe el valor de la altura: "))
        a = b * h
        myFormat = "El area del rectangulo es: {}"
        print(myFormat.format(a))
    except:
        print("\n--> solo puedes escribir numeros, ahora volvera al menu principal. <--\n")

def myCuadrado():
    try:
        print("-- Eligio cuadrado --")
        l = float(input("Escribe el valor del lado: "))
        a = l ** 2
        myFormat = "El area del cuadrado es: {}"
        print(myFormat.format(a))
    except:
        print("\n--> solo pudes escribir numeros, ahora volvera al menu principal. <--\n")

print("-- Programa para calcular el area --")
options = 0
while options != 6:
    try:
        options = int(input("-- menu --\n1.cuadrado 2.rectangulo 3.triangulo 4.pentagono 5.hexagono 6.salir\n--> "))
        if(options == 1):
            myCuadrado()
        if(options == 2):
            myRectangulo()
        if(options == 3):
            myTriangulo()
        if(options == 4):
            myPentagono()
        if(options == 5):
            myHexagono()
    except:
        print("\n--> elige una opcion valida. <--\n")