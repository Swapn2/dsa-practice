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


#  minimul bit flip to convert a to b
a = int(input())
b = int(input())
count = 0
print(decimal_to_binary(a))
print(decimal_to_binary(b))
ans = a^b
for i in range(32):
    if(ans&(1<<i)):
        count +=1

print(count)


