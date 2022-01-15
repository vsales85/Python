#Calculadora Hora Extra
print('Calculadora  HORA EXTRA')
n1=float(input('Digite seu Salário:'))
ho=float(input('Digite numero de horas trabalhadas no Mês:'))
ad = int(input('Digite seu adicional:'))
ht=float(input('HORAS TRABALHADAS'))
soma = (n1/ho*ht)
if ad==30:
    print('Sua hora extra é de: {:.2f}'.format(1.3*soma))
elif ad==50:
    print('Sua hora extra é de: {:.2f}'.format(1.5 * soma))
elif ad==100:
    print('Sua hora extra é de: {:.2f}'.format(2 * soma))
else:
    print('Hora Extra não se aplica')
