#  single number 3

arr= list(map(int,input().split()))
xorr = 0

for i in range(len(arr)):
    xorr = xorr^arr[i]
rightmost = (xorr & (xorr-1))^(xorr)
b1 =0
b2 =0
for i in range(len(arr)):
    if arr[i] & rightmost:
        b1 = b1^arr[i]
    else:
        b2 = b2^arr[i]
print(b1,b2)
