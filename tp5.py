def countno(n):
    a = 0
    if n == 0:
        print(0)
        countno(n - 1)
    if n > 0:
        a = a + 1
        print(-n)
        countno(n - 1)
    if (n < 0) & (a > 0):
        a = a - 1
        print(n)
        countno(n - 1)
countno(3)
