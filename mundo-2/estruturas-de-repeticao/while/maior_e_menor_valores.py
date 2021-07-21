num = int(input('Digite um número:'))
maior = menor = soma = num
cont = 1
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número:'))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    soma += num
    resp = str(input('Quer continuar? [S/N] '))
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
