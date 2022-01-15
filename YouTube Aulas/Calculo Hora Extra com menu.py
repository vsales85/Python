#Calculadora Hora Extra
#while = Enquanto
#op=0 recebe valor 0
#depois do if op =4 para finalizar o programa pois entra em loop infinito

print('Calculadora  HORA EXTRA')
n1=float(input('Digite seu Salário:'))
ho=float(input('Digite numero de horas trabalhadas no Mês:'))
ht=float(input('HORAS TRABALHADAS'))
op = 0
while op != 4:
    print('''        [1] 30%
        [2] 50%
        [3] 100%
        [4] Sair''')
    op = int (input('Qual é sua Opção?:'))
    if op == 1:
        a1 =n1/ho*ht*1.3
        print('Sua hora Extra é:{:.2f}'.format(a1))
        op = 4
    elif op == 2:
        a2 =n1/ho*ht*1.5
        print('Sua hora Extra é:{:.2f}'.format(a2))
        op = 4
    elif op == 3:
        a3 =n1/ho*ht*2
        print('Sua hora Extra é:{:.2f}'.format(a3))
        op = 4
    else:
        print('Volte Sempre !')
