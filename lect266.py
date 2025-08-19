#  print prime factor of a number 
import math

n = int(input())

def prime(n):
    count = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            count +=1
            if n/i != i:
                count +=1
        if count >2:
            break
    if count ==2:
        return True
    else:
        return False
    

#  brute approach 
arr = []
for i in range(1, int(math.sqrt(n))+1):
    if n%i ==0:
        if prime(i):
            arr.append(i)
        if n/i != i:
            if prime(n/i):
                arr.append(int(n/i))
print(arr)
