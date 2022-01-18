print('CALCULADORA  HORA EXTRA')
n1 = float(input('Digite seu Salário: '))
ho = float(input('Digite numero de horas trabalhadas no Mês: '))
dia = int(input('Digite Quantos dias tem o Mês: '))
op = float(input('Digite o Valor de sua Hora Extra 30%: '))
op2 = float(input('Digite o Valor de sua Hora Extra 50%: '))
op3 = float(input('Digite o Valor de sua Hora Extra 100%: '))
opa = (n1/ho)*op*1.3
op2a = (n1/ho*op2)*1.5
op3a = (n1/ho*op3)*2
total = (opa+op2a+op3a)
dsr = 0
while dsr != 3:
    print('''        [1] COM DSR%
        [2] SEM, DSR
        [3] SAIR
        ''')
    dsr = int(input('Qual é sua Opção?:'))
    if dsr == 1:
        fe = int(input('Digite a Quantidade de Feriados e Domingos no Mês'))
        valor = dia - fe
        valor2 = total/valor*fe

        print('O Todata de sua hoa extra é{:.2f}'.format(total+valor2))
        print('Total 30% é :{:.2f} Reais'.format(opa))
        print('Total 50% é :{:.2f} Reais'.format(op2a))
        print('Total 100% é: {:.2f} Reais'.format(op3a))
        print('Sua DSR é: {:.2f} Reais'.format(valor2))
        dsr = 3
    elif dsr == 2:
        print('Total da sua Hora Extra é: {}'.format(total))
        print('Total 30% é :{:.2f} Reais'.format(opa))
        print('Total 50% é :{:.2f} Reais'.format(op2a))
        print('Total 100% é: {:.2f} Reais'.format(op3a))
        dsr = 3
    else:
        print('Continuar')