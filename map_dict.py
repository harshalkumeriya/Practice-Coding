n = int(input())
m = n
print(m)
key = []
value = []

while n > 0:
    key.append(str(input()))
    value.append(int(input()))
    n -= 1

z = dict(zip(key,value))
print(z)

input_key = []
while m > 0:
    m = m-1
    input_key.append(str(input())

for i in input_key :
    if i in key:
        print(z[i])
    else:
        print('Not found')
