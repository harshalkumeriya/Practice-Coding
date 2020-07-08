'''
Task 
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

Note:  is considered to be an even index.

Input Format

The first line contains an integer,  (the number of test cases). 
Each line  of the  subsequent lines contain a String, .
'''

n = int(input())
que = list()
lst1 = list()
lst2 = list()

for i in range(n):
    x = str(input())
    que.append(x)

for i in range(n):
    for j in range(len(que[i])):
        if j % 2 != 0:
            lst1.append(que[i][j])
        else:
            lst2.append(que[i][j])
    aa = "".join(lst2)
    bb = "".join(lst1)
    print('{0} {1}'.format(aa,bb))
    lst1.clear()
    lst2.clear()
          
