opcao=0
print('Calculadora Trabalhador')
salario = float(input('Digite Seu Salário: '))
if opcao != 6:
    print('''        [1] CALCULADORA HORA EXTRA
        [2] CALCULADORA DESCONTO FGTS
        [3] SIMULAÇÃO DE AUMENTO
        [4] DESCONTO DE PASSAGEM SALÁRIO
        [5] CÁCULO IRRF
        [6] SAIR
        ''')
    opcao = int(input('Qual é sua Opção?:'))
if opcao == 1:
    print('CALCULADORA FGTS')
    horastrabalhadasmes = float(input('Carga Horaria Mês: '))
    he30 = float(input('Digite Sua Hora Extra 30%: '))
    he50 = float(input('Digite Sua Hora Extra 50%: '))
    he100 = float(input('Digite Sua Hora Extra 100%: '))
    salm = salario / horastrabalhadasmes
    totalhe = (he30 * 1.30 * salm) + (he50 * 1.50 * salm) + (he100 * 2 * salm)
    opcao = 0
    if opcao != 3:
        print('''            [1] COM DSR%
            [2] SEM, DSR
            [3] SAIR
            ''')
        opcao = int(input('Qual é sua Opção?:'))
    if opcao == 1:
        ht = int(input('Digite Quantos Dias tem esse Mês'))
        fe = int(input('Digite a Quantidade de Feriados e Domingos no Mês'))
        dsr = ht - fe
        dsr2 = (totalhe / dsr) * fe
        print('Sua DSR: {}'.format(dsr2))
        print('Seu Total de Hora Extra é: {:.2f} '.format(totalhe + dsr2))
    if opcao == 2:
        print('Seu Total de Hora Extra é: {:.2f} '.format(totalhe))
    opcao=6
if opcao == 2:
    print('CALCULE O VALOR DESCONTADO DO SEU FGTS:')
    des =salario*8/100
    print('Valor á pagar:{}'.format(des))
if opcao == 3:
    print('SIMULAR AUMENTO')
    aumento = float (input('Digite o Valor Pretendido:'))
    aumento2= salario*aumento/100
    print('SEU SÁLARIO ATUAL É DE {:.2f} E SEU AUMENTO DE SALARIO É {:.2f} TOTALIZANDO {:.2f}:'.format(salario, aumento2,salario+aumento2))
    opcao=6
if opcao == 4:
    print('DESCONTO DE PASSAGEM')
    passagem = salario*6/100
    print('SEU DESCONTO DA PASSAGEM É DE :{} '.format(passagem))
if opcao == 5:
    print('Cálculo IRRF')
    if salario <=1903.98:
        print('INSENTO')

    elif  salario >= 1903.99 and salario<= 2826.65:
        print('Você vai pagar Alíquota 7,5%: {:.2f}'.format(salario*7.5/100-142.80)) #TAXA R$ 142,80

    elif salario >= 2826.66 and salario <= 3751.05:
        print('Você vai pagar Alíquota 15%: {:.2f}'.format(salario*15/100-354.80)) #TAXA R$ 354,80

    elif  salario >= 3751.06  and salario  <=  4664.68:
        print('Você vai pagar Alíquota 22.5%: {:.2f}'.format(salario*22.5/100-663.13)) #TAXA R$636,13
    elif salario  >=  4664.69:
        print('Você vai pagar Alíquota 27.5%: {:.2f}'.format(salario*27.5/100-869.36)) # TAXA R$869,36
else:
    print('Sair')