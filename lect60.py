#  find the Kth missing number (sorted )
#  it is sure that answer will be with in the range of arr means min(arr) to max(arr)

#  brute approach 
# def Kth(nums,k):
#     for i in range(len(nums)):
#         if nums[i] < k:
#             k+=1 
#         else:
#             return k
        

#  BS appraoch 

def Kth(nums , k ):
    low = 0 
    n = len(nums)
    high = n-1

    while(low<=high):
        mid = (low+high)//2
        missing = nums[mid] -(mid+1)
        if missing < k:
            low = mid+1
        else:
            high = mid-1
    return k+high+1              # nums[high] + k - (nums[high] - (high +1))


nums = list(map(int, input().split()))
k = int(input())
print(Kth(nums, k))
