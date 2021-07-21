while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(0, 11):
        print('{} X {:2} = {}'.format(n, c, c*n))
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
