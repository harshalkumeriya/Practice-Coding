arr = [10, 90, 49, 2, 1, 5, 23]
n = len(arr)

for i in range(0, n - 1, 2):
    #current element is smaller than the previous element
    if (i > 0 ) and (arr[i] < arr[i-1]):
        arr[i],arr[i-1] = arr[i-1],arr[i]

    #current element is smaller than the next element
    if (i < n-1) and (arr[i] < arr[i+1]):
        arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)
