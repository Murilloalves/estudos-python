cont = 0
qtde = 10
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = primeiro
while cont < qtde:
    cont += 1
    print('{} → '.format(termo), end='')
    termo += r
    if cont == qtde:
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais?'))
        qtde += mais
print(f'Progressão finalizada com {qtde} termos mostrados.')
