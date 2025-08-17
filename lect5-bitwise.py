#  single number 1 
arr = list(map(int,input().split()))
Xor = 0
for i in range(len(arr)):
    Xor = Xor^arr[i]
print(Xor)

