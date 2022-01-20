print('Quem é o Maior: ')
n1 = float(input('Digite seu Número 1 :'))
n2 = float(input('Digite seu numero 2 :'))
n3 = float(input('Digite seu numero 3 :'))
menor = n1

if  n2<n1 and n2<n3:
    menor =n2
if n3<n1 and n3<n2:
    menor = n3
    print('O Menor Valor Digitado foi {}:'.format(menor))
maior= n1
if n2 > n1 and n2 > n3:
        maior = n2
if n3 > n1 and n3 > n2:
        maior = n3
print('O Maior Valor Digitado foi {}:'.format(maior))