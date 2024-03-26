numeros = []
for i in range(1,21):
    print(i)
    numeros.append(i)

print("the first three items in the list are:")
for i in numeros[:3]:
    print(i)

print("tres items de la mitad de la lista:")
for i in numeros[5:8]:
    print(i)

print("tres items del final de la lista:")
for i in numeros[-3:]:
    print(i)