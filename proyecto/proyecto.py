# Mostar menu al usuario.
# 1.alta 2.baja 3.modificaciones 4.ver alumnos 5.salir.
# agregar, eliminar y modificar.
# alumnnos con calificaciones.
# hasta que el usuario de en salir.
# Programar usando métodos y funcioes#
def myBusqueda(alumno):
    if (alumno in myDictionary):
        print(alumno + " " + str(myDictionary[alumno]))
    else:
        print("no existe el alumno!")

def myEliminar(alumno):
    if (alumno in myDictionary):
        myDictionary.pop(alumno)
    else:
        print("no existe el alumno!")
    return myDictionary

def myMod(alumno):
    if (alumno in myDictionary):
        print(alumno + " " + str(myDictionary[alumno]))
        qualification = float(input("Escribe la nueva calificacion: "))
        myDictionary[alumno] = qualification
    else:
        print("no existe el alumno!")
    return myDictionary

def myAgregar():
    limit = 1
    for x in range(limit):
        alumno = input("Escribe el nombre del alumno: ")
        qualification = float(input("Escribe su calificacion: "))
        myDictionary[alumno] = qualification
    return myDictionary

def myMetodo(options,myDictionary):
    while options != 6:
        if(options == 1):
            print("-- vas a agregar --")
            myAgregar()
        if(options == 2):
            print("-- vas a modificar --")
            alumno = input("Escribe el nombre del alumno para modificar: ")
            myMod(alumno)
        if(options == 3):
            print("-- vas a eliminar --")
            alumno = input("Escribe el nombre del alumno para eliminar: ")
            myEliminar(alumno)
        if(options == 4):
            print("-- va a mostar --")
            print(myDictionary)
        if(options == 5):
            print("-- va a buscar --")
            alumno = input("Escribe el nombre del alumno: ")
            myBusqueda(alumno)
        if(options == 6):
            exit()
        options = int(input("-- Menu de opcion -- \n1.agregar 2.modificar 3.eliminar 4.mostar 5.buscar por nombre 6.salir\n-->"))
myDictionary = {}
options = int(input("-- Menu de opcion -- \n1.agregar 2.modificar 3.eliminar 4.Mostrar 5.buscar por nombre 6.salir\n-->"))
myMetodo(options,myDictionary)