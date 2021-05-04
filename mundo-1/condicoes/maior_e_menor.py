a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
maior = a
menor = a
#Verificando quem é maior
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
#Verificando quem é menor
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O maior valor digitado foi {}'.format(maior))
print('O maior valor digitado foi {}'.format(menor))
