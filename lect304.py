#  trapping the rain water 

nums = list(map(int,input().split()))

prefix = [0]*len(nums)
prefix[0] = nums[0]
for i in range(1,len(nums)):
    prefix[i] = max(prefix[i-1], nums[i])
print(prefix)

suffix = [0]*len(nums)
suffix[len(nums)-1] = nums[len(nums)-1]
for i in range(len(nums)-2,-1,-1):
    suffix[i] = max(suffix[i+1], nums[i])
print(suffix)

total = 0
for i in range(len(nums)):
    leftmax = prefix[i]
    rightmax = suffix[i]
    if nums[i] < leftmax and nums[i] < rightmax:
        total += min(leftmax,rightmax) - nums[i]
print(total)


#  optimal approach 

def findtotal(nums):
    leftmax = 0
    rightmax = 0
    l = 0 
    r = len(nums)-1
    total = 0
    while(l<r):
        if nums[l] <= nums[r]:
            if (leftmax > nums[l]):
                total += leftmax - nums[l]
            else:
                leftmax = nums[l]
            l = l+1
        else:
            if rightmax > nums[r]:
                total += rightmax - nums[r]
            else:
                rightmax = nums[r]
            r = r-1
    return total

print(findtotal(nums))
            
