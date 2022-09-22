
def insertion_sort(A):
    for j in range(1, len(A)):
        key  =  A[j]
        i = j -1
        while(i > -1 and A[i] > key):
            A[i+1] = A[i]
            i = i - 1 
        A[i+1] = key


A = ['Vinicius', 'João', 'Leo', 'Gabriel', 'Henrique', 'Daniel','Ramon', 'Esdras', 'Raniel', 'Diego']
insertion_sort(A)
print(A)

import random
import time

B = []

max =  10000
for i in range(max):
    B.append(random.randint(0,max))

inicio = time.time()    
insertion_sort(B)
fim =  time.time()
print('Tempo transcorrido = {}'.format(fim-inicio))
print(B)

#entrada
C = ['maria', 10, 20, 'josé', 'antônio', 30, 20, 40]
# saída
R = ['antônio', 'josé', 'maria', 10,20,20,30,40]


