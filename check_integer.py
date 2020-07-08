#check digit
def is_int(x):
  absolute = abs(x)
  print("absolute=",absolute)
  rounded = round(absolute)
  print("rounded=",rounded)
  return absolute - rounded

z = float(input("Give number: "))
check_int = is_int(z)
if check_int == 0 :
    print("given number is integer which is ",z)
else :
    print(str(z) + " number is not integer")
#check is sum
def digit_sum(n):
  sum = 0
  str_n = str(n)
  for number in str_n :
    sum += int(number)
  return sum

#another way to add sum of the digit

def sum_of_digit(num) :
    summ = 0
    while num != 0 :
        remain = num % 10
        summ += remain
        num = num // 10
    return summ

summation = sum_of_digit(123)
print(summation)