from random import randint
comp = randint(0, 10)
tentativa = 1
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
print(comp)
palpite = int(input('Qual seu palpite? '))
while palpite != comp:
    tentativa += 1
    if palpite < comp:
        print('Mais... Tente mais uma vez!')
    else:
        print('Menos... Tente mais uma vez!')
    palpite = int(input('Qual seu palpite? '))
print(f'Acertou com {tentativa} tentativas. Parabéns!')
