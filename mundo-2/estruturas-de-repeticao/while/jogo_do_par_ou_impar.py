from random import randint
vitoria = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    op = ' '
    comp = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + comp
    while op not in 'PI':
        op = str(input('Par ou Ímpar? [P/I] ')).upper()
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {comp}. Total de {soma} deu', end=' ')
    print('PAR' if soma % 2 == 0 else 'ÍMPAR')
    print('-' * 30)
    if op == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif op == 'I':
        if soma % 2 == 0:
            print('Você PERDEU!')
            break
        else:
            print('Você VENCEU!')
            vitoria += 1
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes.')
