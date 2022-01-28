qto = int (input('Quantidade de Aluno: '))
i =0
soma = 0
while i < qto:
    nome = str (input('Digite Seu Nome: '))
    idade = int(input('Digite A Idade do {}: Aluno: {} '.format(nome,i+1)))
    soma =soma +idade
    i +=1
media = soma/qto
print('A Média de Idade da Turma é {}'.format(media))
print(mv)