arr = [12, 11, 13, 5,5,5,5,5,5,55, 6]
print(arr)
def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
insertionsort(arr)
print(arr)
            
