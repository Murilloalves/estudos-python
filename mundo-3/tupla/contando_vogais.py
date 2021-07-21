palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis',
'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aáeiou':
            print(letra, end=' ')
