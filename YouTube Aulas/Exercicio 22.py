# Crie um Programa que leia o seu nome completo de uma pessoa e mostre:
#o nome com todas a letras maiucsula
#o nome com todas letras mnusculas
#quantas letras aotodo sem considerar o espaço
#quantas letras tem o primeiro nome

nome= (input('Digite seu Nome:')).strip()
print ('Seu nome com Letras Maiúsculas é: {}'. format(nome.upper()))
print('Seu Nome com Letras Minusculas é: {} '.format(nome.lower()))
print ('Seu nome tem ao todo: {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem: {} letras'.format(nome.find(' ')))