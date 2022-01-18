# r somente leitura
# w Escrita (caso o arquvo já exista ele será apagado e um novo arquivo será criado)
# a leitura e escriva ( adiciona novo arquivo e o novo conteudo ao fim do arquivo)
# r+ Leitura e escrita
# w+ escrita (o modo w tambem apaga conteudo anterior do arquivo)
# a+ elitura e escrita (abre o aquivo para atualização)

arquivo = open('teste.txt')
ler = arquivo.readlines ()
for ler2 in ler: #Ler linha Separadas
    print(ler2 )
