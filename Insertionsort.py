def Insertionsort(A):
    # initialize indexes
    j = 0

    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while A[i] > key and i >= 0:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key


    return A

_list = [2,4,1,59,12,4]
Insertionsort(_list)
print(_list)
