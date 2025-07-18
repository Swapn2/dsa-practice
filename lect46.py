#  lower bound ( smallest index such that arr[index] >= x)

def lower_bound(arr,k):
    n = len(arr)
    high = n-1
    low = 0
    ans = n
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
    ans = n
    while (low <= high):
        mid = (low+high)//2
        if arr[mid] > k:
            ans = mid
            high = mid-1 
        else:
            low = mid+1
    return ans 

#  search insert position 
#  if k already exist in the array insert at lower_bound = basically return index of lower_bound , if not index of just higher one which comes from lowe_bound 


def search_insert_position(arr,k):
    return lower_bound(arr,k)

#  floor  = largest no. in array <= x
#  ceil = smallest array in the array >=x

def ceil(arr,k):
    i=  lower_bound(arr,k)
    return arr[i]

def floor(arr, k):
    i = upper_bound(arr,k) -1
    return arr[i]






arr = list(map(int, input().split()))
k = int(input())

print(lower_bound(arr,k))
print(upper_bound(arr,k))
print(search_insert_position(arr,k))
print(ceil(arr,k))
print(floor(arr,k))