a,b = 0,1
n = 0
num = 5
lst = [0,1]
while (n < num ):
    n = a + b
    a, b = b,n
    lst.append(n)

print(lst)
    
    
