import math
A = [-1,8,15,24,0,6,16,22]

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

print(merge(A,0,3,7))
assert merge(A,0,3,7)== [-1, 0, 6, 8, 15, 16, 22, 24]
