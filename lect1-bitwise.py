#  convert decimal to binary 

def decimal_to_binary(n):
    result = ""
    while(n >1):
        if n%2 ==1:
            result = result + '1'
        else:
            result = result + '0'
        n = int(n/2)
    result = result +str(n)
    return result[::-1]


def binary_to_decimal(s):
    num = 0 
    pow2 = 1
    for i in range(len(s)-1,-1,-1):
        if s[i] == '1':
            num = num + pow2
        pow2 = pow2*2
    return num



n = int(input())
ans = decimal_to_binary(n)
print(ans)
deci = binary_to_decimal(ans)
print(deci)

    
