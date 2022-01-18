#Faça um progrma que leia um número de 0 9999 e mostre na tela cada um dos digitos separados
#exemplo 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar 1

n=int  (input('Informe Um Numero entre 0 a 9999: '))
u= n //1 % 10
d= n //10% 10
c= n //100 % 10
m= n //1000 % 10
if n < 0:
    print('Não Usamos Numeros Negativos')
elif n <= 9999:
    print('Unidade:{}'.format(u))
    print('Dezena:{}'.format(d))
    print('Centena:{}'.format(c))
    print('Milhar:{}'.format(m))
else:
    print('Favor Digitar um número entre (0 a 9999)')