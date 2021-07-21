from random import choice, randint
from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in num:
    print(n, end=' ')
print(f'\nO maior número é {max(num)}')
print(f'O menor número é {min(num)}')
"""num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
maior = 0
menor = 0
print('Os valores sorteados foram: ', end='')
for n in range(1, 6):
    escolhido = choice(num)
    print(escolhido, end=' ')
    if n == 1:
        maior = escolhido
        menor = escolhido
    else:
        if escolhido > maior:
            maior = escolhido
        if escolhido < menor:
            menor = escolhido
print(f'\nO maior número é {maior}')
print(f'O menor número é {menor}')"""
