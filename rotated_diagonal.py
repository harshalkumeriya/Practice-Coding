import numpy as np
arr = np.arange(1,10).reshape(3,3)
r_len, c_len = arr.shape
for row in range(r_len):
    for col in range(c_len):
        if (row+col+1) == r_len:
            arr[row][col] = 0
print(arr)
