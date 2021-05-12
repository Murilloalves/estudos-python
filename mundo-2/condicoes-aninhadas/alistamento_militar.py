from datetime import date
print('---- Alistamento Militar ----')
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18-idade))
    print('Seu alistamento será em {}.'.format(atual+(18-idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} ano(s).'.format(idade-18))
    print('Seu alistamento foi em {}.'.format(atual+(18-idade)))
else:
    print('Você deve se alistar IMEDIATAMENTE!')
