
# Read the variable from STDIN
a = int(input())
#print('interger ',a)
# Output the variable to STDOUT
input_list = [int(input()) for _ in range(a)]
print('numbers ',input_list)
for k,v in enumerate(input_list):
    #print('key ', k, ' + ','value',v)
    x = 0
    while v > 0:
        x += (v % 10) ** 3
        v //= 10
    #print(x)
    if x == input_list[k]:
        print('It is an ARMSTRONG number')
    else:
        print('It is NOT an ARMSTRONG number')
