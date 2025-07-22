#  koko eating banana - return the min value of k such that koko can eat the all banana with h hours
#  k = no of banana per hour 

import math
def timeneed(arr,k):
    totaltime = 0
    for i in range(len(arr)):
        totaltime += math.ceil(arr[i]/k)
    return totaltime


#  k will be in range (1  to max of pile )
# def kokoeat(arr,h):
#     for i in range(1,max(arr)):
#         if timeneed(arr,i) == h:
#             return i
#     return -1

#  using BS

def kokoeat(arr,h):
    low = 1
    ans = -1
    high = max(arr)
    while(low <= high):
        mid = (low+high)//2
        if timeneed(arr,mid) <= h:
            ans = mid
            high = mid -1
        else:
            low = mid+1
    return ans




piles = list(map(int , input().split()))
h = int(input())
print(kokoeat(piles,h))