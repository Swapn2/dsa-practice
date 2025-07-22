# #  search in the sorted rotated array having duplicate element 
#  here we cant tell about index by using BS we can just ensure that present or not 
# for getting index we need to use LS

def search(arr, k ):
    low = 0 
    n = len(arr)
    high = n-1

    while(low <= high):
        mid  = (low + high)//2
        if arr[mid] == k:
            return True
        if arr[mid] == arr[low] and arr[high] == arr[low]:
            high = high -1
            low = low +1
            continue
        if arr[low] <= arr[mid]:
            # left sorted
            if arr[mid] >= k and arr[low] <= k:
                high = mid -1
            else:
                low = mid+1 
        else:
            # right sorted 
            if arr[mid] <= k and arr[high] >= k:
                low = mid+1
            else:
                high = mid-1 
    return False 


arr= list(map(int , input().split()))
k = int(input())
print(search(arr,k))