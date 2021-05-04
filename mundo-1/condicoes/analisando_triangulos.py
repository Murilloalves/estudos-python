print('=-' * 20)
print('Analisador de Triângulos')
print('=-' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos PODEM FORMAR um triângulo!')
else:
    print('Os segmento NÃO PODEM FORMAR um triângulo!')
