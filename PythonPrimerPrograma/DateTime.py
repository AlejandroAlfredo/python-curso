import datetime
x = datetime.datetime.now()
print("[ fecha ]")
print(x)  # fecha

print("[ years ]")
print(x.year)  # years

print("[ nombre del dia ]")
print(x.strftime('%A'))  # lun,mar,mie...

print("[ nombre del mes ]")
print(x.strftime('%b'))  # mes

print("[ abreviacion del dia ]")
print(x.strftime('%a'))

print("[ %w]")
print(x.strftime('%W'))

print("[ numero del mes ]")
print(x.month)  # mes numeros

print("[ numero del dia ]")
print(x.day)  # dias numeros

print("[ Alterando la fecha ]")
x = datetime.datetime(2019, 5, 17)
print(x)
