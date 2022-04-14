#Dictionary
myAlumnos = {
    "juan" : 10,
    "modelo" : "1987",
    "auto" : "audi"
}
print(myAlumnos)
#agregando un elemento
myAlumnos["pepe"] = 100
if("juan" in myAlumnos):
    print("si existe")
else:
    print("no existe")
# imprimiendo toda los datos
#for x,y in myAlumnos.items():
        #print(x)
# quitando un elemento
myAlumnos.pop("juan")
dir2 = myAlumnos.copy()
myAlumnos.clear()
print(myAlumnos)
print(dir2)