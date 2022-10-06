import math
A = [7,8,9,11,100,-1,0,4,6,7,9,10,11,300,999,10000000,5,6,7,9]

# codigo 

def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r - q
    L = [0] * (n1+1)
    R = [0] * (n2+1)
    for i in range(0,n1):
        L[i] = A [p+i]
    for j in range(0,n2):
        R[j] =  A[q+j+1]
    L[n1] = math.inf
    R[n2] = math.inf
    i = 0
    j = 0
    for k in range(p,r+1):
        if(L[i] <= R[j]):
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j +1
    return A

def merge_sort(A,p,r):
    if(p < r):
        q = (p+r)//2 # resultado inteiro da divisão
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

print('antes: ', A)
merge_sort(A,0,len(A)-1)
print('depois: ' , A)