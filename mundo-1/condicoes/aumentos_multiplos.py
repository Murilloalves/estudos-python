salario = float(input('Qual é salário do funcionário? R$'))
if salario <= 1250:
    aumento = salario + (salario*15/100)
else:
    aumento = salario + (salario * 10 / 100)
print('Quem ganhava R${} passa a ganhar R${:.2f} agora.'.format(salario, aumento))
