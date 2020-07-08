import string
num = 3
lst = []
alpha = string.ascii_lowercase
pat = alpha[:num]
for i in range(num):
    lst.append(pat[i:num] + pat[::-1][1:])
print(lst)
