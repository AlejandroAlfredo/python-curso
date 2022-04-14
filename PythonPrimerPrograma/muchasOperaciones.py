print("Sumas")
valueOne = int(input("Escribe el primer valor: "))
valueTwo = int(input("Escribe el segundo valor: "))
resultado = valueOne + valueTwo
print("El resultado de la suma es: " + str(resultado))


print("\nRestas")
valueOne = int(input("Escribe el primer valor: "))
valueTwo = int(input("Escribe el segundo valor: "))
resultado = valueOne - valueTwo
print("El resultado de la resta es: " + str(resultado))

print("\nMultiplicacion")
valueOne = int(input("Escribe el primer valor: "))
valueTwo = int(input("Escribe el segundo valor: "))
resultado = resultado = valueOne * valueTwo
print("El resultado de la mutiplicacion es: " + str(resultado))

print("\nDivision")
valueOne = int(input("Escribe el primer valor: "))
valueTwo = int(input("Escribe el segundo valor: "))
resultado = resultado = valueOne / valueTwo
print("El resultado de la division es: " + str(resultado))

print("\nMenu de operaciones")
options = int(input("Elige una opcion: \n1.Suma 2.Resta 3.Multiplicacion 4.Division\n"))
if(options == 1):
    print("\n-- suma --")
    valueOne = int(input("Escribe el primer valor: "))
    valueTwo = int(input("Escribe el segundo valor: "))
    resultado = valueOne + valueTwo
    print("El resultado de la suma es: " + str(resultado))

if(options == 2):
    print("\n-- resta --")
    valueOne = int(input("Escribe el primer valor: "))
    valueTwo = int(input("Escribe el segundo valor: "))
    resultado = valueOne - valueTwo
    print("El resultado de la resta es: " + str(resultado))

if(options == 3):
    print("\n-- multiplicacion --")
    valueOne = int(input("Escribe el primer valor: "))
    valueTwo = int(input("Escribe el segundo valor: "))
    resultado = resultado = valueOne * valueTwo
    print("El resultado de la mutiplicacion es: " + str(resultado))

if(options == 4):
    print("\n-- division --")
    valueOne = int(input("Escribe el primer valor: "))
    valueTwo = int(input("Escribe el segundo valor: "))
    resultado = resultado = valueOne / valueTwo
    print("El resultado de la division es: " + str(resultado))