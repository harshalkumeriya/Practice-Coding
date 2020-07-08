import numpy as np
#n = int(input())
arr = np.arange(1,10).reshape(3,3)

arr[:,0] = 0

arr[:,-1] = 0

arr[0,:] = 0

arr[-1,:] = 0

print(arr)
