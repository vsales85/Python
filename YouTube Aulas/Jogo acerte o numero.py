import random
print('Acerte o Número')
num = random.randint (0,5)
adv = int (input('Digite um número entre 0 e 5 e Tente Acertar o Número' ))
if num==adv:
    print('Parabens VocÊ Acertou o Número')
elif adv>5:
    print('Numero Invalido')
else:
    print('Você Errou Tente Novamente')