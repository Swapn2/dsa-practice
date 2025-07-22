#  minimum in rotated sorted array  having unique element 

def minimum(arr):
    low = 0 
    n = len(arr)
    high = n-1
    ans = int(1e18)
    while( low <= high):
        mid = (low + high) //2
        if arr[mid]  >= arr[low]:
            ans = min(arr[low] ,ans)
            low = mid+1
        else:
            ans = min(ans , arr[mid])
            high = mid-1
    return ans




arr = list(map(int , input().split()))
print(minimum(arr))