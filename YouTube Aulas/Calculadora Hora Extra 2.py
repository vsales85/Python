
print('CALCULADORA  HORA EXTRA')
n1 = float(input('Digite seu Salário: '))
ho = float(input('Digite numero de horas trabalhadas no Mês: '))
dia = int(input('Digite Quantos dias tem o Mês'))
fe = int(input('Digite a Quantidade de Feriados e Domingos no Mês'))
op = float (input('Digite o Valor de sua Hora Extra 30%'))
op2 = float (input('Digite o Valor de sua Hora Extra 50%'))
op3 = float (input('Digite o Valor de sua Hora Extra 100%'))
dj = dia-fe
opa = (n1/ho)*op*1.3
op2a = (n1/ho*op2)*1.5
op3a = (n1/ho*op3)*2
total = (opa+op2a+op3a)
dsr=total/dj*fe
valor=total+dsr
print ('Total 30% é :{:.2f} Reais'.format(opa))
print ('Total 50% é :{:.2f} Reais'.format(op2a))
print ('Total 100% é :{:.2f} Reais'.format(op3a))
print('Total de Hora Extra {:.2f}'.format(total))
print('Sua DSR é de: {:.2f} Reais'.format(dsr))
print ('total da hora Extra e DSR é {:.2f} Reais'.format(valor))