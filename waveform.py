arr = [10, 90, 49, 2, 1, 5, 23] 
print("input array: ",arr)
#sort the array 
arr.sort() 
print("Sorted array : ",arr) 
# Swap adjacent elements 
for i in range(0,len(arr)-1,2):
    arr[i], arr[i+1] = arr[i+1], arr[i]

print("waveform array : ",arr)


