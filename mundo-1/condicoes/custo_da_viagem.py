distancia = float(input('Qual é a distância da sua viagem? '))
print('você etá prestes a comencar uma viagem de {}Km.'.format(distancia))
# preco = distancia * 0.50 if distancia <=200 else distancia * 0.45
if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
