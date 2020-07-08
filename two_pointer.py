input_lists = [[5,9,10],[1,3,4,7,11]]
list2 = input_lists[0]
list1 = input_lists[1]

L1, L2 = len(list1), len(list2)
x = list()
i ,j = 0,0

# Write your code here
while i < L1 and j < L2 :
    if list1[i] > list2[j]:
        x.append(list2[j])
        j += 1
        while   j == L2 and i < L1 :
           x.append(list1[i])
           i +=1
           
    else:
        x.append( list1[i])
        i += 1
        while  i == L1 and  j < L2:
            x.append(list2[j])
            j += 1

print(x) 
    
