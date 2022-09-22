entrada = open('entrada.in', 'r')
saida = open('saida_maior.out', 'w')
linhas = entrada.readlines()

for l in linhas:
    valores  = l.split(' ')
    valores_int = [int(e) for e in valores]
    maior = valores_int[0]
    for v in valores_int:
        if v > maior:
            maior = v
    saida.write(str(maior)+ '\n')

            