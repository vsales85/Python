#Ver maior e menor numero digitado
print ('Aumento Salarial')
sal = float(input('Digite o seu Salario:'))
if sal >=1250:
    aumento = sal*10/100
    print('O Seu novo salario é de: {}'.format(sal+aumento))
else:
    aumento2 = sal * 15 / 100
    print('O seu Novo salario é {}'.format(sal+aumento2))