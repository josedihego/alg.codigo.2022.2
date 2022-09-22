

arquivo = open('entrada.in', 'r')
arquivoSaida = open('saida_soma.out', 'w')
linhas = arquivo.readlines()

for l in linhas:
    numeros  = l.split(' ')
    soma = 0
    for n in numeros:
        soma = soma + int(n)
    arquivoSaida.write(str(soma))  
    arquivoSaida.write('\n') 