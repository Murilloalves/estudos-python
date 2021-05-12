peso = float(input('Qual é seu peso?(Kg) '))
alt = float(input('Qual é sua altura? (m) '))
imc = peso / alt ** 2
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
print('Você está', end=' ')
if imc <= 18.5:
    print('ABAIXO DO PESO')
elif imc <= 25:
    print('na faixa de PESO IDEAL.')
elif imc <= 30:
    print('em SOBREPESO.')
elif imc <= 40:
    print('em Obesidade, cuidado!')
else:
    print('em OBESIDADE MÓRBIDA, procure um médico IMEDIATAMENTE!!')
