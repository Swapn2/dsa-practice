#  binary search  (BS) implementation in Python

# # iterative appraoch
def search_in_bs(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    while (low <= high):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid 
        elif arr[mid] > target:
            high = mid-1
        elif arr[mid] < target:
            low = mid +1
    return -1

#  recurssive approach 


# def search(arr, low , high,target):
#     if low >high:
#         return -1 
#     mid = (low+high)//2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         low = mid+1
#         return search(arr, low, high,target)
#     else:
#         high = mid-1
#         return search(arr, low , high,target)

# def search_in_bs(arr,target):
#     n = len(arr)-1
#     return search(arr, 0,n,target)








arr = list(map(int , input().split()))
k = int(input())
print(search_in_bs(arr,k))