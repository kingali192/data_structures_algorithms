# Merge two sorted Python lists S1 and S2 into properly sized list S
def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i<len(S1) and S1[i]<S2[j]):
            S[i+j] == S1[i]
            i += 1
        else:
            S[i+j] == S2[j]
            j += 1
    return S   

def merge_sort(S):
    n = len(S)//2
    if n < 2:
        return
    S1 = S[0:n]
    S2 = S[n:]
    merge_sort(S1)
    merge_sort(s2)
    merge(S1, S2, S)

if __name__ == '__main__':
    array1 = [1,2,3,4,5]
    array2 = [6,7,8,9,10]
    array3 = []
    merge(array1, array2, array3)
    print(array3)
    
             
    
    
    