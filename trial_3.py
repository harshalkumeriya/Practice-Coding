lst = [12,2,34,54,4,7,88]
print(lst)
lst.sort()
for i in range(0,len(lst) - 2,2):
    if lst[i] < lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)
    
