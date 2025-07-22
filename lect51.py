#  find the no array has been rotated having unique element only 

def rotation(arr):
    low = 0
    n = len(arr)
    high = n-1
    index = -1
    ans = int(1e18)

    while(low <= high):
        mid = (low+high)//2
        if arr[mid] <= arr[high]:
            if arr[mid] <= ans:
                ans = arr[mid]
                index = mid
                low = mid+1
        if arr[mid] >= arr[low]:
            if arr[low] <= ans:
                ans = arr[low]
                index = low
                high = mid -1 
    print('hi')
    return {ans , index}


arr = list(map(int, input().split()))
print(rotation(arr))