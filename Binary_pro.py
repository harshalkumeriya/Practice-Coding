x = bin(int(input()))
x = x.lstrip('0b')
z,count = 0,-1
result = list()
for i in x:
    count +=1
    if i == '1':
        z +=1
        if (len(x)-1) == count:
            result.append(z)
    else:
        result.append(z)
        z = 0
print(max(result))
