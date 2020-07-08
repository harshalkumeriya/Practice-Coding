'''For a sorted list L (sorted in an ascending order), containing ‘n’ integers,
find if there exists a pair of elements in the list — whose sum is equal to ‘S’.'''

def twosum(L, S):
    n = len(L)
    i = 0
    j = n - 1
    
while i < j:
    if L[i] + L[j] == S:
        return True
    elif L[i] + L[j] < S:
        i += 1
    else:
        j -= 1
return False
                     
