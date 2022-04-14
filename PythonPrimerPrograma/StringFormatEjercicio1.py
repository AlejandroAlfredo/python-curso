#1. Pedir nombre
#2. pedir edad (int)
#3. pedir estatua en metros
#final imprimir datos en una linea
#usando string format
name = input("Escribe tu nombre: ")
old = int(input("Escribe tu edad: "))
long = float(input("Escribe tu estatura: "))

myFormat = "{} tu edad es: {}, tu estatura es {:.2f}m"
print(myFormat.format(name,old,long))