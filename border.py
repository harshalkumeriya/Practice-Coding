import numpy as np

n = int(input('Enter the number : '))

def border(n):
    x = np.zeros((n,n), dtype = int)

    x[:,0] = 1
    x[:,n-1] = 1
    x[0,:] = 1
    x[n-1,:] = 1

    print(x)

border(n)


### Read the variable from STDIN
##n = int(input())
##
##import numpy as np
##
### Create an 'n*n' array of all ones
##border_array = np.ones((n, n), dtype = int)
##
### Fill the array with zeroes from second index (i.e. index 1) to second last index.
### Do this for both row indices and column indices
##border_array[1:-1, 1:-1] = 0
##
### Print the array created
##print(border_array)
