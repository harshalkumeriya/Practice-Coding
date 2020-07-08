input_list = [1, 31, 4, 9, 7, 114, 6, 13]

n = len(input_list)

print(input_list)
def func(arr, n):
    flag = 1
    while(flag):
        flag = 0
        for i in range(0,n-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = 1
               
func(input_list, n)
print(input_list[n-2])
