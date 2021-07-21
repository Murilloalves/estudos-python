print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
qtde = int(input('Quantos termos você quer mostrar? '))
cont = 2
t1 = 0
t2 = 1
print('{} → {} →'.format(t1, t2), end='')
while cont != qtde:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(' {} → '.format(t3), end='')
    cont += 1
print('Fim!')
