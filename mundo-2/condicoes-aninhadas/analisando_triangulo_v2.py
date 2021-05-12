n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3 == n1:
        triangulo = 'Equilátero'
    elif n1 != n2 != n3 != n1:
        triangulo = 'Escaleno'
    else:
        triangulo = 'Isósceles'
    print('Os segmentos acima PODEM FORMAR um triângulo {}.'.format(triangulo))
else:
    print('Os segmento acima NÃO PODEM FORMAR um triângulo.')