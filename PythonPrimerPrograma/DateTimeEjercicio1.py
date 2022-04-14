# en base a la fecha de hoy
# indicar la fecha de hace 9 dias
# e imprimir el dia
import datetime
x = datetime.datetime.now()
print("-- fecha de hoy --")
print(x)
mes = x.month
year = x.year
day = x.day
fecha = day - 9
print("-- hace 9 dias --")
x = datetime.datetime(year,mes,fecha)
print(x)
print(x.strftime('%A'))