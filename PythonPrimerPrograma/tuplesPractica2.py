#1. Crear tuple con numeros, e indicar el numero mas alto y el mas bajo.
def funcionPrincipal(tuples, list):

    for x in tuples:
        list.append(x)
        list.sort(reverse=True)
    return list
list = []
tuples = (1,20,5,3,4,2)
resultado = funcionPrincipal(tuples,list)
print(resultado)
print("-- resultados --")
print("numero mas alto: " + str(resultado[0]))
print("numero mas bajo: " + str(resultado[5]))