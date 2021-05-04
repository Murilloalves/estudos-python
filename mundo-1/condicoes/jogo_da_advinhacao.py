from random import randint
comp = randint(0, 5)
print('-=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 30)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
if num == comp:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(comp, num))
