#  Nth root of the integer 
#  if == M 0
# if < M 1
#  if > M 2
def power(mid,n,M):
    ans = 1
    for i in range(n):
        ans = ans * mid
        if ans > M:
            return 2
    if ans == M:
        return 0
    else:
        return 1 



def Nth(n,M):
    low = 1 
    high = M
    while(low <= high):
        mid = (low+high)//2
        if power(mid,n,M) == 0:
            return mid
        elif power(mid,n,M) ==1:
            low = mid+1
        else:
            high = mid -1
    return -1


n = int(input())
M = int(input())
print(Nth(n,M))