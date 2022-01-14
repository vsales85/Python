# O Mesmo Professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
#Faça um programa qie çeia o nome dos quatro alunos e mostra a ordem sorteada

import random
nome=input('Aluno 1:')
nome1=input('Aluno 2:')
nome2=input('Aluno 3:')
nome3=input('Aluno 4:')
lista=[nome,nome1,nome2,nome3]
random.shuffle (lista)
print('A Ordem desses  Alunos é:')
print('{}'.format(lista))