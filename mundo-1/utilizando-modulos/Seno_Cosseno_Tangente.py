from math import radians, sin, cos, tan
angulo = int(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} te o SENO de {}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} te o COSSENO de {}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} te o TANGENTE de {}'.format(angulo, tangente))
