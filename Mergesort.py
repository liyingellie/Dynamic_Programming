def Mergesort(A,p,r):

    if p < r:
        m = (p+r)//2
        Mergesort(A,p,m)
        Mergesort(A,m+1,r)
        Merge(A,p,m,r)
        return A

def Merge(A,p,m,r):

    # replicate two arrays
    L = []
    R = []
    x = 0
    y = 0

    n1 = m-p+1
    n2 = r-m

    L = A[p:m]
    R = A[m+1:r]


    # reorder
    k = 0
    i = 0
    j = 0

    for k in range(p-1,r):
        if L[i] >= R[j]:
            A[k] = R[j]
            j = j+1

        else:
            A[k] = L[i]
            i = i + 1

    return A

_list = [2,4,1,59,12,4]
Mergesort(_list,0,len(_list))
print(_list)
