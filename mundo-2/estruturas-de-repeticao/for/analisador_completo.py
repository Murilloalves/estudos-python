somaidade = 0
cont = 0
maioridadeHomem = 0
nomeVelho = ''
contFem = 0
for p in range(1, 5):
    print(f'---- {p}ª Pessoa ----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    cont += 1
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm':
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade <= 20:
        contFem += 1
media = somaidade / cont
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print(f'O homem mais velho tem {maioridadeHomem} anos.')
print(f'Ao todo são {contFem} mulheres com menos de 20 anos.')
