livings = ['mirko', 'betty', 'cesar']
deceases = ['mario', 'patricia', 'auramaria']
invites = livings

print(f'buenos días invites {invites[0].title()} está usted invitado')
print(f'buenos días invites {invites[1].title()} está usted invitado')
print(f'buenos días invites {invites[2].title()} está usted invitado')

print(f'buenos días, {invites[1].title()} no podrá asistir')
del invites[1]

print(f'buenos días invites {invites[0].title()} está usted invitado')
print(f'buenos días invites {invites[1].title()} está usted invitado')