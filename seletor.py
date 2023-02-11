import random

friends = [
    'Joao',
    'Maria',
    'Elisa',
    'Joana',
    'Gustavo',
    'Salomão',
    'Leonardo',
    'Amy',
    'Bruna'
]

# random.randint(1, 5) --> número aleatório entre 1 e 5
# random.choice(array) --> item aleatório neste array

selected = random.choice(friends) # escolha aleatoriamente um amigo

print('Com quem devo conversar hoje?')
print(selected)