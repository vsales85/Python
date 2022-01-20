print('Controle de Transito')
vl = float(input('Digite a Velocidade:  '))
if vl>80:
    multa =vl-80
    multa2 =multa*7.00
    print('Você foi Multado em {} Reais'.format(multa2))
else:
    print('Parabens Continue Respeitando a Sinalização')