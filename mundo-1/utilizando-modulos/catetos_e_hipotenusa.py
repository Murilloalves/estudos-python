from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adja = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(oposto, adja)))
