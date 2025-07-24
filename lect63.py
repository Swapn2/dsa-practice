#  painter's partition or  split array larest sum 


# def minunit(arr,painter):
#     k = max(arr)
#     n = sum(arr)
#     for i in range(k,n+1):
#         if sumunit(arr,i) == painter:
#             return i


def sumunit(arr,units):
    sum=0
    painter = 1
    for i in range(len(arr)):
        if arr[i] +sum > units:
            painter +=1
            sum = 0
        sum += arr[i]
    return painter


# BS approach 
def minunit(arr,painter):
    low = max(arr)
    high = sum(arr)
    ans = -1
    while(low <= high):
        mid = (low+high)//2
        if sumunit(arr,mid) <= painter:
            ans = mid
            high = mid -1
        else:
            low = mid +1
    return ans 

arr = list(map(int, input().split()))
painters = int(input())
print(minunit(arr,painters))
