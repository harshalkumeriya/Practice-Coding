import ast,sys
import numpy as np
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
diffArray=np.diff(np.sign(np.diff(input_list)))
maximas=list(np.where(diffArray == -2)[0] + 1)
maximas=[int(x) for x in maximas]
print(maximas)
#below is an alternate approach
#from scipy.signal import argrelextrema
#maximas=argrelextrema(ser.values, np.greater)[0]
