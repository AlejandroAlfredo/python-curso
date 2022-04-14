# pedir una edad y si es invalido pedir un numero valido
try:
    old = int(input("Escribe tu edad: "))
except:
    print("Escribe un numero valido")
finally:
    print("adios")