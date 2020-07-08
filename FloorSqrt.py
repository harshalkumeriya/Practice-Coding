def floorSqrt(x):
    if (x == 0 or x == 1):
        return x
    i = 1
    result = 1
    while result < x:
        i +=1
        result = i * i
        if result == x:
            return i
    return i - 1
x = 169
print(floorSqrt(x))
