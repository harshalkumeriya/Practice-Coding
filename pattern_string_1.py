n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(64+ i+1), end ='')
    print()

'''
A
BB
CCC
DDDD
EEEEE
'''
