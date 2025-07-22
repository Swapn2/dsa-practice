#  search in the sorted rotated array having unique element 

def search(arr,k):
    low = 0 
    n = len(arr)
    high = n-1
    while ( low <= high ):
        mid = (low+high)//2
        if arr[mid] == k:
            return mid
        if arr[low] <= arr[mid]:
            # left half sorted 
            if arr[low] <= k and arr[mid] >= k:
                high = mid -1
            else:
                low = mid+1
        else:
            # right half sorted
            if k >= arr[mid] and k <= arr[high]:
                low = mid+1
            else:
                high = mid -1
    return -1  


arr = list(map(int , input().split()))
k = int(input())
print(search(arr,k))