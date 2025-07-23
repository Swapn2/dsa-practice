#  least capacity to ship the package within D days 
#  range of answer should be max(weights) to sum(weights)  think carafully why ?

def leastcap(weights , days):
    low = max(weights)
    high = sum(weights)
    ans = -1
    while(low <= high):
        mid = (low+high)//2
        if day(weights,mid) <= days:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

def day(weights, cap):
    load = 0
    day = 1
    for i in range(len(weights)):
        if load + weights[i] > cap:
            day = day+1
            load = 0
        load += weights[i]
    return day
#  instead of Bs we can also use the for loop but it will be high TC

weights = list(map(int, input().split()))
days = int(input())
print(leastcap(weights,days))    
