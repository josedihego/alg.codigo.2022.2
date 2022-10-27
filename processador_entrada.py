
arquivo =  open('entrada_exemplo.in', 'r')
linhas = arquivo.readlines()
arquivo_saida = open('saida_exemplo.out', 'w')

saida = ''
for l in linhas:
    conteudo = l.split(' ')
    conteudo[-1] = conteudo[-1].replace('\n','')
    soma = 0
    for e in conteudo:
        if e.isnumeric():
            soma = soma + int(e)
        else:
            if(soma==0):
                saida =  saida + e
            else:
                saida = saida + ' '+ str(soma) + ' ' + e
                soma = 0
    saida = saida + ' '+ str(soma)
    arquivo_saida.write(saida+ '\n')
    saida = ''
    
