def myQuinsena(elPago):
        resultado = elPago * 15
        return resultado

def myMensual(elPago):
        resultado = elPago * 30
        return resultado

name = input("Cual es su nombre?: ")
elPago = int(input("Cuanto te pagan a diario?: "))
options = int(input("quieres calcular la: \n1.quinsena? 2.mensualidad?"))
if(options == 1):
    resultado = myQuinsena(elPago)

if(options == 2):
    resultado = myMensual(elPago)

print("" + name + " su Pago es: " + str(resultado))