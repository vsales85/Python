#Faça um programa que leia o comprimento do cateto oposto e do cateto adjcente
#de um Triângulo retângulo , calcule e moste o comprimento da hipotenusa
#****Exemplo 1 matemática sem importação
import math
comp = float(input('Digite Comprimento do Cateto Oposto: '))
comp2 = float(input('Digite Comprimento do Cateto: '))
#****Exemplo 1 hi=(comp ** 2 + comp2 ** 2 ) ** (1/2)
#****Exemplo 1 print('A Hipotenusa vai medir {:.2f}'.format(hi))

hi=math.hypot(comp,comp2)
print ('A Hipotenusa é: {:.2f}'.format(hi))