num = int(input('Informe um número: '))
n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(n))
print('Unidade: {}\nDezena: {}\n'
      'Centena: {}\nMilhar: {}\n'.format(u, d, c, m))
