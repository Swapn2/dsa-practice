#   aggressive cows (min distance between is maximum)

#  answer range ( 1 to max-min) think about it first 


# def minDist(arr, cows):
#     arr.sort()
#     n = arr[len(arr)-1] - arr[0]
#     for i in range(1,n+1):
#         if canweplace(arr,i,cows) == True:
#             # print(i)
#             continue
#         else:
#             return i-1
        
def canweplace(arr,dist,cows):
    count = 1
    lastcord = arr[0]
    for i in range(len(arr)):
        if arr[i] - lastcord >= dist:
            lastcord = arr[i]
            count +=1
    # print(count)
    if count >= cows:
        return True
    else:
        return False
    
#  BS approach 
def minDist(arr,cows):
    arr.sort()
    low = 1
    high = arr[len(arr)-1] - arr[0]
    ans =-1
    while(low <= high):
        mid = (low+high)//2
        if canweplace(arr,mid,cows) == True:
            low = mid+1
            ans = mid
        else:
            high = mid -1
    return ans

arr = list(map(int, input().split()))
cows = int(input())
print(minDist(arr,cows))
# print(canweplace(arr,1,4))