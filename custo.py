
# somatorio de 1 até 100 com for
v = 100
soma = 0
for j in range(1,v+1):
    soma =  soma + j

print('Forma 1 : {}'.format(soma))

soma2 = int((v * (v+1))/2)

print('Forma 2 : {}'.format(soma2))