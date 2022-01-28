print('VAMOS CALCULAR')
numero = int(input('Digite um Numero: '))
numero2 = int(input('Digite Outro Numero: '))
opcao = 0
while opcao !=4:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] NOVOS NUMEROS
[4] SAIR DO APP''')
    opcao = int(input('Qual é sua opção: '))
    if opcao==1:
        print('A SOMA ENTRE O NUMERO {} E  NUMERO {} E IGUAL A {} '.format(numero,numero2,numero+numero2))
    elif opcao == 2:
        print('A MULTIPLICAÇÃO ENTRE O NUMERO {} E  NUMERO {} E IGUAL A {} '.format(numero,numero2,numero*numero2))
    elif opcao ==3:
        numero = int(input('Digite um Numero: '))
        numero2 = int(input('Digite Outro Numero: '))
    elif opcao==4:
         print('SAir do app')
