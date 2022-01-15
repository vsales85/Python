#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno e cosseno e tangente desse ângulo.

import math
ang = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians((ang)))
print('O Angulo de {} tem o Seno de  {:.2f}'.format(ang,seno))
coss = math.cos(math.radians(ang))
print ('Angulo de {} tem o Cosseno de {:.2f}'.format(ang,coss))
tang = math.tan(math.radians(ang))
print ('Angulo de {} tem a Tangente{:.2f}'.format (ang,tang))
