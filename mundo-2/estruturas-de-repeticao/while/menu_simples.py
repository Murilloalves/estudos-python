n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
maior = n1
sair = False
while not sair:
    print('=-=' * 15)
    print('''[ 1 ] soma
[ 2 ] multiplicador
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    op = int(input('Qual sua opção?'))
    if op == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif op == 2:
        print('{} x {} == {}'.format(n1, n2, n1*n2))
    elif op == 3:
        if n2 > n1:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif op == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        sair = True
    else:
        print('Opção inválida. Tente novamente')
