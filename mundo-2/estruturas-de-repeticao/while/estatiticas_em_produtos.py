print('{:-^40}'.format('LOJA SUPER BARATÃO'))
total = prod1000 = prodBarato = cont = 0
nomeBarato = ' '
while True:
    resp = ' '
    produto = str(input('Nome dp Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        prod1000 += 1
    if cont == 1 or preco < prodBarato:
        prodBarato = preco
        nomeBarato = produto
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {prod1000} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeBarato} que custa R${prodBarato:.2f}')
