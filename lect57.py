#  Find the minimum no of days to make M bouquets

def possible(arr,mid,n,k):
    count = 0 
    noofB= 0
    for i in range(len(arr)):
        if arr[i] <= mid :
            count +=1
        else:
            noofB += count//k
            count = 0
    noofB += count//k
    if noofB >= n:
        return True
    return False



def boolday(arr,n,k):
    low = min(arr)
    high = max(arr)
    ans = -1
    while(low <= high):
        mid = (low+high)//2
        if possible(arr, mid,n,k) == True:
            ans = mid 
            high = mid-1
        else:
            low = mid+1
    return ans 







bloomdays = list(map(int ,input().split()))
n = int(input()) # no of bouque 
k = int(input()) # adjacent flower required 
print(boolday(bloomdays,n,k))