times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
               'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
               'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
               'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('\n{:=^30}'.format(' BRASILEIRÃO 2018 '))
print('-=' * 15)
print(f'Lista de Times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem Alfabética {sorted(times)}')
print('-=' * 15)
print(f'O fluminense está na posição {times.index("Fluminense") + 1}')
print('-=' * 15)
