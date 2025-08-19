#  printing divisor of a number 
n = int(input())

#  brute approach 
# arr =[]
# for i in range(1,n+1):
#     if n%i ==0:
#         arr.append(i)
# print(arr)


#  optimal approach 
import math
arr =[]
for i in range(1,int(math.sqrt(n))+1):
    if n%i ==0:
        arr.append(i)
        if n/i != i:
            arr.append(int(n/i))
print(arr)