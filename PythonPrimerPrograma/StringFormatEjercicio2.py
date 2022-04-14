#1. pedir nombre,si el nombre tiene mas de 7 letras imprimir el nombre e indicar que el nombre es largo
name = input("Escribe tu nombre: ")
if(len(name) > 7):
    myFormat = "{} tu nombre es muy largo"
    print(myFormat.format(name))
else:
    myFormat = "tu nombre: {}"
    print(myFormat.format(name))