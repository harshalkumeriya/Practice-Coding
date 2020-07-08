#Input values
numbers = input().split(',')
print(numbers)
#Init result values to 0 (neutral number)
result = 0

#We iterate the array and perform a xor operation between each value
#Since the xor of paired values is equal to 0, only the unpaired will be left in result
for number in numbers:
    print(number, '+', result)
    result = result ^ int(number)

#Output value
print(result)
