#Calculadora Hora Extra
#while = Enquanto
#op=0 recebe valor 0
#depois do if op =4 para finalizar o programa pois entra em loop infinitot
print('CALCULADORA  HORA EXTRA')
n1=float(input('Digite seu Salário: '))
ho=float(input('Digite numero de horas trabalhadas no Mês: '))
dia=int(input('Digite Quantos dias tem o Mês'))
dsr=int(input('Digite a Quantidade de Feriados e Domingos no Mês'))
dia2=dia-dsr
op = 0
ht=float(input('HORAS TRABALHADAS: '))

while op != 4:
    print('''        [1] 30%
        [2] 50%
        [3] 100%
        [4] Sair''')
    op = int (input('Qual é sua Opção?:'))
    if op == 1:
        a1 =n1/ho*ht*1.3
        aa1 =a1/dia*dsr
        print('Sua hora Extra é:{:.2f} e seu Dsr é de {}:' .format(a1,aa1))
        op = 4
    elif op == 2:
        a2 =n1/ho*ht*1.5
        aa2 = (a2 / dia2) * dsr
        print('Sua hora Extra é:{:.2f} e Sua DSR é {}'.format(a2,aa2))
        op = 4
    elif op == 3:
        a3 =n1/ho*ht*2
        aa3 =(a3/dia2)*dsr
        print('Sua hora Extra é:{:.2f} e Sua DSR é de :{}'.format(a3,aa3))
        op = 4
    else:
        print('Volte Sempre !')
c