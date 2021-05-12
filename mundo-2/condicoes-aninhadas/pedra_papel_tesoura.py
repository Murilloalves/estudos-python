from time import sleep
from random import randint
opcoes = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('=== GAME: JOKENPO ===')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
if 2 >= jogador >= 0:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    sleep(0.5)
    print('-=' * 15)
    print('Computador jogou {}'.format(opcoes[comp]))
    print('Jogador jogou {}'.format(opcoes[jogador]))
    print('-=' * 15)
    if comp == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('O JOGADOR venceu!')
        else:
            print('O COMPUTADOR venceu!')
    elif comp == 1:
        if jogador == 0:
            print('O COMPUTADOR venceu!')
        elif jogador == 1:
            print('EMPATE!')
        else:
            print('O JOGADOR venceu!')
    else:
        if jogador == 0:
            print('O JOGADOR venceu!')
        elif jogador == 1:
            print('O COMPUTADOR venceu!')
        else:
            print('EMPATE!')
else:
    print('Opção inválida!')
