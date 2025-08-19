#  seive of eratothenes

# Q1 . given a number print all the prime till n
import math
n = int(input())

prime = [1]*(n+1)

for i in range(2,int(math.sqrt(n))+1 ):
    if prime[i] ==1:
        for j in range(i*i, n+1, i):
            prime[j] =0
arr = []
for i in range(2,n+1):
    if prime[i]==1:
        arr.append(i)
print(arr)
