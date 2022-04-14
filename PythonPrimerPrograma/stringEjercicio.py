# 1.pedir una cadena al usuario e imprimir
    # 1. si tiene algun caracter alfanumerico.
    # 2. si tiene algun caracter alfabetico.
    # 3. si tiene algun digito.
    # 4. si tiene alguna minuscula.
    # 5. si tiene alguna mayuscula.
print("1. si tiene algun caracter alfanumerico.")
value1 = input("Esbribe una palabra: ")
print(value1.isalnum())
print("2. si tiene algun caracter alfabetico.")
value2 = input("Esbribe una palabra: ")
print(value2.isalpha())
print("3. si tiene algun digito.")
value3 = input("Esbribe una palabra: ")
print(value3.isdigit())
print("4. si tiene alguna minuscula.")
value4 = input("Esbribe una palabra: ")
print(value4.islower())
print("5. si tiene alguna mayuscula.")
value5 = input("Esbribe una palabra: ")
print(value5.isupper())