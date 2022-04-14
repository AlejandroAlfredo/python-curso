# Strings
# string multiline
a = """Hola mundo
y mas,esto es
otra tes"""
# print(a)
print((a[2]))
# subString
print("-- substring --")
print(a[5:10])
#
a = " Holamundo! "
print("-- Strip --")
print(a.strip())
print("-- len --")
print(len(a))
print("-- lower --")
print(a.lower())
print("-- upper --")
print(a.upper())
print("-- replace --")
print(a.replace("H","L"))
#print(a.split(" "))
print("-- split --")
word="Hola-mundo-crudo"
myArrays = word.split("-")
print(myArrays)
print("-- join --")
a = ["hola","mundo","irreal"]
print("-".join(a))