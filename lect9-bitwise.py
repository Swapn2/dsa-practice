#  divide two integer 

dividend = int(input())
divisor = int(input())

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    if a == 0:
        return 0

    sign = 1
    if (a < 0) ^ (b < 0):
        sign = -1

    n = abs(a)
    d = abs(b)
    ans = 0

    while n >= d:
        counter = 0
        while n >= (d << (counter + 1)):
            counter += 1
        ans += (1 << counter)
        n -= (d << counter)

    return sign * ans
print(divide(dividend,divisor))