#  single element in a sorted array

#  brute approach

def single_element(arr):
    n = len(arr)
    if n==1:  return arr[0]

    for i in range(n):
        if arr[0] != arr[1]:
            return arr[0]
        elif arr[n-1] != arr[n-2]:
            return arr[n-1]
        elif (arr[i] != arr[i+1] and arr[i] != arr[i-1]):
            return arr[i]
    return -1


#  BS approach 

def single_element(arr):
    n = len(arr)
    if n==1: return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    elif arr[n-1] != arr[n-2]:
        return arr[n-1]
    low = 1
    high = n-2
    while(low <= high):
        mid = (low+high)//2
        if arr[mid] != arr[mid+1] and arr[mid] != arr[mid-1]:
            return arr[mid]
        elif (mid%2 ==1 and arr[mid-1] == arr[mid]) or (mid %2 ==0 and arr[mid] == arr[mid+1]): # this region is in left half
            low = mid+1  # so eliminating the left half
        elif (mid%2 ==1 and arr[mid+1] == arr[mid]) or (mid %2 ==0 and arr[mid] == arr[mid-1]): # this region is in right half
            high = mid-1  # so eliminating the right half 
    return -1


arr = list(map(int , input().split()))
print(single_element(arr))