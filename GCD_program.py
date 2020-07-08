a = int(input())
b = int(input())
small ,res= 0,0
if a == b:
    res = a

elif a > b:
    small = b
    
else:
    small = a

for i in range(1,small+1):
    if (a % i == 0) and (b % i == 0):
        res = i

print(res)
