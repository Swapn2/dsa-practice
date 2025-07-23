#  find the smallest divisor given a threshold 
"""
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
"""

import math

def smallestDivisor(nums , threshold):
    low = 1 
    high = max(nums)
    ans = -1
    while(low <= high):
        mid = (low+high)//2
        if sum(nums,mid) <= threshold:
            ans = mid
            high = mid -1
        else:
            low = mid+1
    return ans
def sum(nums,k):
    s = 0
    for i in range(len(nums)):
        s += math.ceil(nums[i]/k)
    return s


nums = list(map(int,input().split()))
threshold = int(input())
print(smallestDivisor(nums,threshold))