paises = ['peru', 'venezuela','chile','argentina','ecuador']
print(paises)
paises.append('bolivia')
print('se agregó un país')
print(paises)
print('se retira el pais argentina')
paises.remove("argentina")
print(paises)
print('se retira el pais venezuela')
del paises[1]
print(paises)
print('se retira el pais que está al final')
paises.pop()
print(paises)

print('Se muestra la lista al revez')
paises.reverse()
print(paises)

