#  next smaller element (monotonic stack)

nums = list(map(int,input().split()))

def nse(nums):
    s = []
    ans = []
    for i in range(len(nums)):
        while len(s) !=0 and s[-1] >= nums[i]:
            s.pop()
        if len(s) ==0:
            ans.append(-1)
        else:
            ans.append(s[-1])
        s.append(nums[i])
    return ans

print(nse(nums))