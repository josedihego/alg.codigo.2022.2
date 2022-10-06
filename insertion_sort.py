
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


#entrada
C = ['maria', 10, 20, 'josé', 'antônio', 30, 20, 40]
C1 = []
C2 = []
for v in C:
    if(type(v)==str):
        C1.append(v)
    else:
        C2.append(v)   
insertion_sort(C1)    
insertion_sort(C2)      

# saída
R = C1 + C2
print(R)


