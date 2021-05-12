print('===== LOJAS ALVES =====')
preco = float(input('Preço das compras: R$'))
print('''Formas DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    novoPreco = preco - (preco*10/100)
elif op == 2:
    novoPreco = preco - (preco*5/100)
elif op == 3:
    novoPreco = preco
    parcela = novoPreco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
else:
    qtda = int(input('Quantas parcelas? '))
    novoPreco = preco + (preco*20/100)
    parcela = novoPreco / qtda
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(qtda, parcela))
print('Sua compra de R${} vai custar R${} no final'.format(preco, novoPreco))
