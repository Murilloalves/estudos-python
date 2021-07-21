n = int(input('Digite um número para\ncalcular seu Fatorial: '))
c = n
acumulador = 1
print(f'{n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    acumulador *= c
    c -= 1
print(f'{acumulador}')
# n = int(input('Digite um número para\ncalcular seu Fatorial: '))
# cal = 1
# print('Calculando {}! = '.format(n), end='')
# for c in range(n, 0, -1):
#     cal *= c
#     print(f'{c} ', end='')
#     print('x 'if c > 1 else '=', end='')
# print(f' {cal}')
