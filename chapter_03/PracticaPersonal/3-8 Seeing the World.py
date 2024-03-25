places = ['england', 'japan', 'france', 'germany', 'brazil']
print("list en orden original")
print(places)
print("lista ordenada sin modificar lista original")
print(sorted(places, reverse=False))
print("lista ordenada al revez sin modificar lista original")
print(sorted(places, reverse=True))
print("list en orden original")
print(places)

print("cambiar el orden de la lista con reverse")
places.reverse()
print(places)
print("cambiar el orden de la lista nuevamente")
places.reverse()
print(places)
print()


print("lista ordenada modificando la lista original")
#Aca se ordena y se deja ordenado.
places.sort(reverse=False)
#Aca se muestra lo ordenado.
print(places)

print("lista ordenada al revez  modificando la lista original")
#Aca se ordena y se deja ordenado.
places.sort(reverse=True)
#Aca se muestra lo ordenado.
print(places)