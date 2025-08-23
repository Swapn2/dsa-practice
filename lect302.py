#  next greater element (monotonic stack) 2 : circular array 

nums = list(map(int,input().split()))

def NGE(nums):
    s = []
    ans = []
    n = 2*len(nums)-1
    for i in range(n, -1,-1):
        while(len(s)!=0 and s[-1] <= nums[i%(len(nums))]):
            s.pop()
        if i<len(nums):
            if len(s)==0:
                ans.append(-1)
            else:
                ans.append(s[-1])
            # break
        s.append(nums[i%len(nums)])
        # break
    return ans

print(NGE(nums))
