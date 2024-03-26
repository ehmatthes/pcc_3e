pizzas = ['pepperoni', 'vegetales', 'queso']
for pizza in pizzas:
    print(pizza)
    print(f'me gusta la pizza de {pizza}')

friend_pizzas = pizzas[:]
pizzas.append('alemana')
friend_pizzas.append('napolitana')

print("mis pizzas favoritas son")
for pizza in pizzas:
    print(pizza)

print()
print("Las pizas favoritas de mis amigos son:")
for pizza in friend_pizzas:
    print(pizza)
