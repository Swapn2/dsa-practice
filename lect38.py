#  num of subarray with XOR = k 

def subarray(arr,k):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            xor = 0
            for m in range(i,j+1):
                xor = xor^arr[m]
            if xor == k:
                count +=1 
    return count 


# better 
def subarray1(arr,k):
    n = len(arr)
    count = 0
    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor = xor^arr[j]
            if xor == k:
                count +=1 
    return count 

# optimal 
def subarray2(arr,k):
    n = len(arr)
    hash = {}
    hash[0] = 1
    xr = 0
    count = 0
    for i in range(n):
        xr = xr^arr[i]
        x = xr^k
        if x in hash:
            count = count + hash[x]
        if xr not in hash:
            hash[xr] = 1
        else:
            hash[xr] +=1
    return count 





arr = list(map(int , input().split()))
k = int(input())
print(subarray(arr,k))
print(subarray1(arr,k))
print(subarray2(arr,k))