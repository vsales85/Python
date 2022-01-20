print('Calculadora FGTS')
salario = float(input('Digite Seu Salário: '))
horastrabalhadasmes = float (input('Carga Horaria Mês: '))
he30 = float(input('Digite Sua Hora Extra 30%: '))
he50 = float(input('Digite Sua Hora Extra 50%: '))
he100 = float(input('Digite Sua Hora Extra 100%: '))
salm= salario/horastrabalhadasmes
totalhe = (he30*1.30*salm)+(he50*1.50*salm)+(he100*2*salm)
opcao = 0
if opcao != 3:
    print('''        [1] COM DSR%
        [2] SEM, DSR
        [3] SAIR
        ''')
    opcao = int(input('Qual é sua Opção?:'))
if opcao == 1:
    ht = int(input('Digite Quantos Dias tem esse Mês'))
    fe = int(input('Digite a Quantidade de Feriados e Domingos no Mês'))
    dsr=ht-fe
    dsr2=(totalhe/dsr)*fe
    print('Sua DSR: {}'.format(dsr2))
    print('Seu Total de Hora Extra é: {:.2f} '.format(totalhe+dsr2))
elif opcao == 2:
    print('Seu Total de Hora Extra é: {:.2f} '.format(totalhe))
else:
    print('Sair')

