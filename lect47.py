
#  first and last occurence 

#  lower bound ( smallest index such that arr[index] >= x)

def lower_bound(arr,k):
    n = len(arr)
    high = n-1
    low = 0
    ans = -1
    while (low <= high):
        mid = (low+high)//2
        if arr[mid] >=k:
            ans = mid
            high = mid-1 
        else:
            low = mid+1
    return ans 

#  upper bound (smallest index such that arr[idx] > x )

def upper_bound(arr,k):
    n = len(arr)
    high = n-1
    low = 0
    ans = -1
    while (low <= high):
        mid = (low+high)//2
        if arr[mid] > k:
            ans = mid
            high = mid-1 
        else:
            low = mid+1
    return ans

def occurence_pos(arr,k):
    first = lower_bound(arr,k)
    last = upper_bound(arr,k) -1 
    print(first)
    print(last)
    if first < 0 or last < 0:
        return None
    else:
        return last-first+1

arr = list(map(int, input().split()))
k = int(input())
print(occurence_pos(arr,k))