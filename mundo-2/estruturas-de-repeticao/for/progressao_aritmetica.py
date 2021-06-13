print('=' *20)
print('10 TERMOS DE UMA PA')
print('=' *20)
primeiro = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = primeiro + (10 - 1) * r
for i in range(primeiro, decimo + r, r):
    print('{}'.format(i), end=' → ')
print('Acabou')
