num = 10
final = []
lst = list(range(1,num+1))

for i in range(1,num+1):
    final.append(lst[:i])

print(final)
