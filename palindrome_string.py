string=input()
from collections import Counter 
res = Counter(string)
print(res)
count=0
for key in res:
    print(key)
    if (res[key]%2!=0) & (count==1):
        print('1st')
        count=2
        break
    if (res[key]%2!=0) & (count==0):
        print('2nd')
        count=1
if(count>1):
    print('No')
else:
    print('Yes')
