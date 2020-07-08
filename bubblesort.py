arr = [64, 34, 25, 12, 22, 22, 22, 11, 90]
print(arr)

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(0,n-i-1):
           if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]
               flag = 1
        if flag == 0:
            break

bubblesort(arr)
print(arr)
