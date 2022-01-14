#Calculadora Hora Extra
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
        print('Sua hora Extra é:{}'.format(a1))
    elif op == 2:
        a2 =n1/ho*ht*1.5
        print('Sua hora Extra é:{}'.format(a2))
    elif op == 3:
        a3 =n1/ho*ht*2
        print('Sua hora Extra é:{}'.format(a3))
    else:
        print('Volte Sempre!')
