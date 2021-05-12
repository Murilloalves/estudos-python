n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if n1 < 0 or n2 < 0 or n1 > 10 or n2 > 10:
    print('Notas somente entre 0 e 10.')
else:
    print('Tirando {} e {}, a média do aluno é {:.1f}'.format(n1, n2, media))
    if media > 7:
        print('O aluno está APROVADO.')
    elif 7 > media >= 5:
        print('O aluno está em RECUPERAÇÃO.')
    else:
        print('O aluno está REPROVADO.')
