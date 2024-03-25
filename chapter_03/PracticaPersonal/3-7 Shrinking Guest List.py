invites = ['betty', 'marcela', 'patricia', 'mariana', 'sandra', 'martha']
print(f'buenos días {invites} ha encontrado una mesa más grande')

invites.insert(0, "viviana")
invites.insert(2,"carolina")
invites.append("margarita")

print(f'buenos días {invites[0]} bienvenido (a)')
print(f'buenos días {invites[1]} bienvenido (a)')
print(f'buenos días {invites[2]} bienvenido (a)')
print(f'buenos días {invites[3]} bienvenido (a)')

print(f'buenos días {invites[4]} bienvenido (a)')
print(f'buenos días {invites[5]} bienvenido (a)')
print(f'buenos días {invites[6]} bienvenido (a)')
print(f'buenos días {invites[7]} bienvenido (a)')

print(f'buenos días {invites[8]} bienvenido (a)')

print("Disculpen, solo se podrán invitar dos personas")

print(f'Disculpe {invites.pop()} No podrá asistir por limite de personas')
print(f'Disculpe {invites.pop()} No podrá asistir por limite de personas')
print(f'Disculpe {invites.pop()} No podrá asistir por limite de personas')
print(f'Disculpe {invites.pop()} No podrá asistir por limite de personas')
print(f'Disculpe {invites.pop()} No podrá asistir por limite de personas')
print(f'Disculpe {invites.pop()} No podrá asistir por limite de personas')
print(f'Disculpe {invites.pop()} No podrá asistir por limite de personas')

print(f'Buenos días {invites[0]} usted sigue invitado a la fista')
print(f'Buenos días {invites[1]} usted sigue invitado a la fista')

del invites[1]
del invites[0]
print(invites)