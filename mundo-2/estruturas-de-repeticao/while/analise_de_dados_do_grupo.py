maioridade = totH = totM20 = 0
while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    sexo = ' '
    resp = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper()
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {totH} Homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
