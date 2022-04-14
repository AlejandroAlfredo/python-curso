# 1.pedir una cadena al usuario e imprimir
    # 1. si tiene algun caracter alfanumerico.
    # 2. si tiene algun caracter alfabetico.
    # 3. si tiene algun digito.
    # 4. si tiene alguna minuscula.
    # 5. si tiene alguna mayuscula.
def myUpper(value, list):
    for x in value:
        list.append(x.isupper())
    if(True in list):
        print("-- Mayusculas --")
        print("True")
    else:
        print("-- Mayusculas --")
        print("False")
    list.clear()

def myLowerCase(value, list):
    for x in value:
        list.append(x.islower())
    if(True in list):
        print("-- minusculas --")
        print("True")
    else:
        print("-- minusculas --")
        print("False")
    list.clear()

def myDigits(value, list):
    for x in value:
        list.append(x.isdigit())
    if(True in list):
        print("-- digitos --")
        print("True")
    else:
        print("-- digitos --")
        print("False")
    list.clear()

def myAlpha(value, list):
    for x in value:
        list.append(x.isalpha())
    if(True in list):
        print("-- alfabetico --")
        print("True")
    else:
        print("-- alfabetico --")
        print("False")
    list.clear()

def myAlphaNum(value, list):
    for x in value:
        list.append(x.isalnum())
    if(True in list):
        print("-- alfanumerico --")
        print("True")
    else:
        print("-- alfanumerico --")
        print("False")
    list.clear()
list = []
value = input("Escribe una cadena de texto: ")
myAlphaNum(value, list)
myAlpha(value, list)
myDigits(value, list)
myLowerCase(value, list)
myUpper(value, list)