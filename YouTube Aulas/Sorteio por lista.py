#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, Lendo o Nome deles e escrevendo o nome do escolido
#Lista fica entre [].

import random
nome=input('Aluno 1:')
nome1=input('Aluno 2:')
nome2=input('Aluno 3:')
nome3=input('Aluno 4:')
lista=[nome,nome1,nome2,nome3]
escolhido= random.choice (lista)
print('O Aluno escolido foi {}'.format(escolhido))