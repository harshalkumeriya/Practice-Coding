import numpy as np

input_list = [[1,2,3,4,5,6,7,8,9],2.75]
array=np.array(input_list[0])
n=input_list[1]
print(array[(np.abs(array-n)).argmin()])
