n1 = float(input('Digite Nota 1'))
n2 = float(input('Digite Nota 2'))
n3 = float(input('Digite Nota 3'))
n4 = float(input('Digite a Nota 4'))
total= (n1+n2+n3+n4)/4
if total <=4:
    print('Reprovado')
elif total ==5:
    print('Recuperação')
else:
    print(''
          'Aprovado')