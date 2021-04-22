valor = int(input('Uma distância em metros: '))
dm = valor * 10
cm = valor * 100
mm = valor * 1000
dam = valor / 10
hm = valor / 100
km = valor / 1000
print('{}dm\n{}cm\n{}mm'.format(dm, cm, mm))
print('{:.2f}dam\n{:.2f}hm\n{:.2f}km'.format(dam, hm, km))

