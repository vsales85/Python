print('''
         [M] MASCULINO
         [F] FEMENINO''')
sexo = 1
while sexo !=0:
    sexo = str (input('Digite Seu Sexo: ')).strip().upper()[0]
    if sexo == 'M':
        print('MASCULINO')
        sexo=0
    elif sexo == 'F':
        print('FEMENINO')
        sexo=0
    else:
        print('Erro Tente Novamente')