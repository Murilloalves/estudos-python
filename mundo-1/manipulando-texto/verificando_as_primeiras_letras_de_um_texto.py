print('Vendo se a cidade começa com SANTO ou não!')
cid = str(input('Em que cidade você nasceu? ')).strip()
separa = cid.split()
print(separa[0].lower() == 'santo')
