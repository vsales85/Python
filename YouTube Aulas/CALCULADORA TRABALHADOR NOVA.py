opcao=0
print('Calculadora Trabalhador')
salario = float(input('Digite Seu Salário: '))
if opcao != 6:
    print('''        [1] CALCULADORA HORA EXTRA
        [2] CALCULADORA DESCONTO INSS
        [3] SIMULAÇÃO DE AUMENTO
        [4] DESCONTO DE PASSAGEM SALÁRIO
        [5] CÁCULO IRRF
        [6] SAIR
        ''')
    opcao = int(input('Qual é sua Opção?:'))
if opcao == 1:
    print('CALCULADORAHORA EXTRA')
    horastrabalhadasmes = float(input('Carga Horaria Mês: '))
    he30 = float(input('Digite Sua Hora Extra 30%: '))
    he50 = float(input('Digite Sua Hora Extra 50%: '))
    he100 = float(input('Digite Sua Hora Extra 100%: '))
    salm = salario / horastrabalhadasmes
    totalhe = (he30 * 1.30 * salm) + (he50 * 1.50 * salm) + (he100 * 2 * salm)
    opcao = 0
    if opcao != 3:
        print('''            [1] COM DSR%
            [2] SEM, DSR''')
        opcao = int(input('Qual é sua Opção?:'))
    if opcao == 1:
        ht = int(input('Digite Quantos Dias tem esse Mês'))
        fe = int(input('Digite a Quantidade de Feriados e Domingos no Mês'))
        dsr = ht - fe
        dsr2 = (totalhe / dsr) * fe
        print('Sua DSR: {:.2f}'.format(dsr2))
        print('Seu Total de Hora Extra é: {:.2f} '.format(totalhe + dsr2))
    if opcao == 2:
        print('Seu Total de Hora Extra é: {:.2f} '.format(totalhe))
    opcao=6
if opcao == 2:
    print('VALOR DESCONTADO DO SEU INSS:')
    if salario<=1212:
        print('Seu Desconto é de 7.5% eo valor descontato do seu salario é {:.2f}'.format(salario*7.5/100))
    elif salario >=1212.01 and salario <= 2427.35:
        print('Seu Desconto é de 9% eo valor descontato do seu salario é{:.2f}'.format(salario*9/100))
    elif salario >=2427.36 and salario <=3641.03:
        print('Seu Desconto é de 12% eo valor descontato do seu salario é{:.2f}'.format(salario*12/100))
    elif salario >=3641.04 and salario<=7087.22:
        print('Seu Desconto é de 14% eo valor descontato do seu salario é{:.2f}'.format(salario*12/100))
    elif salario >7087.22:
        print('Seu Desconto é de 828,39')
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
    des = salario * 8 / 100
    dependentes = int(input('Digite Numeros de Dependentes'))
    dependentes2 = dependentes*189.59
    irrf = salario-(dependentes2+des)
    valor1 = irrf*7.5/100-142.80
    valor2 = irrf*15/100-354.80
    valor3 = irrf*22.5/100-663.13
    valor4 = irrf*27.5/100-869.36
    if salario <=1903.98:
        print('INSENTO')
    elif salario >= 1903.99 and salario<= 2826.65 and valor1 <= 0:
        print('Sua Alíquota 7,5 FOI ISENTO DEVIDO AO NUMERO DE DEPENDENTES')
    elif salario >= 1903.99 and salario <= 2826.65:
        print('Você vai pagar Alíquota 7,5%: {:.2f}'.format(valor1)) #TAXA R$ 142,80
    elif salario >= 2826.66 and salario <= 3751.05 and valor2 <= 0:
        print('Sua Alíquota 15% FOI ISENTO DEVIDO AO NUMERO DE DEPENDENTES')
    elif salario >= 3751.06  and salario  <=  4664.68:
        print('Sua Alíquota 22,5% FOI ISENTO DEVIDO AO NUMERO DE DEPENDENTES')
    elif salario >= 2826.66 and salario <= 3751.05:
        print('Você vai pagar Alíquota 15%: {:.2f}'.format(valor2)) #TAXA R$ 354,80
    elif salario >= 3751.06  and salario  <=  4664.68 and valor3 <= 0:
        print('Você vai pagar Alíquota 22.5%: {:.2f}'.format(valor3)) #TAXA R$636,13
    elif salario  >=  4664.69 and valor3 <= 0:
        print('Sua Alíquota 27,5% FOI ISENTO DEVIDO AO NUMERO DE DEPENDENTES')
    elif salario  >=  4664.69:
        print('Você vai pagar Alíquota 27.5%: {:.2f}'.format(valor4)) #TAXA R$869,36
else:
    print('Sair')