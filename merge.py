
A = [-1,8,15,24,0,6,16,22]

# codigo 

def merge(A,p,q,r):
    n1 = q - p +1
    n2 =  r - q
    L = A[p:q+1]
    R = A[q+1:r+1]
    i =0
    j = 0
    for k in range(p,r+1):
        if(i==len(L) or j == len(R)):
            if(i==len(L) and j < len(R)):
                A[k] = R[j]
                j =  j +1
            elif(j==len(R) and i < len(L)):
                A[k] = L[i]
                i = i +1
        else:
            if L[i] <= R[j]:
                A[k] =  L[i]
                i = i + 1
            else:
                A[k] =  R[j]
                j = j + 1
    return A

print(merge(A,0,3,7))
assert merge(A,0,3,7)== [-1, 0, 6, 8, 15, 16, 22, 24]
