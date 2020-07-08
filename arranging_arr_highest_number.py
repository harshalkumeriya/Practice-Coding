from itertools import permutations

arr = [12,21,23]
res = []
x = list(permutations(arr, len(arr)))
for i in x:
    res.append("".join(map(str,i)))

print(x)
print(res)
print(max(res))
