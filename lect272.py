# two pointer / sliding window 

# 1. constant window 
# Q. we have to find the maxsum subarray of length = k

# arr = list(map(int,input().split()))
# k  = int(input())
# l = 0 
# r = k-1
# sum = 0
# maxsum = 0
# for i in range(k):
#     sum = sum+arr[i]
# while(r<len(arr)-1):
#     maxsum = max(maxsum,sum)
#     sum = sum-arr[l]
#     l+=1
#     r+=1
#     sum = sum+arr[r]
# print(maxsum)

# 2. longest subarray / substring sum <= k
# Q. longest subarray with sum <=k:

#  brute approach 

# arr = list(map(int,input().split()))
# k = int(input())
# maxlen = 0 
# for i in range(len(arr)):
#     sum = 0 
#     for j in range(i,len(arr)):
#         sum = sum+arr[j]
#         if sum <= k:
#             maxlen = max(maxlen , j-i+1)
#         elif sum >k:
#             break
# print(maxlen)

#  better approach 

# arr = list(map(int,input().split()))
# k = int(input())
# l = 0
# r = 0 
# sum = 0
# maxlen = 0
# while(r<len(arr)):
#     sum = sum +arr[r]
#     while(sum >k):
#         sum = sum - arr[l]
#         l+=1
#     if sum<=k:
#         maxlen = max(maxlen, r-l+1)
#     r+=1
# print(maxlen)

# optimal way 

# arr = list(map(int,input().split()))
# k = int(input())
# l = 0
# r = 0 
# sum = 0
# maxlen = 0
# while(r<len(arr)):
#     sum = sum +arr[r]
#     if(sum >k):
#         sum = sum - arr[l]
#         l+=1
#     if sum<=k:
#         maxlen = max(maxlen, r-l+1)
#     r+=1
# print(maxlen)

# 3. Number of subarray where <condition>

# Q. findthe number of subarray with sum = k:

arr = list(map(int,input().split()))
k = int(input())

def noofsubarray(arr,k):
    l = 0
    r = 0
    count = 0
    sum= 0
    while(r<len(arr)):
        sum = sum + arr[r]
        while(sum > k):
            sum= sum - arr[l]
            l+=1
        if sum <= k:
            count+=r-l+1
        r+=1
    return count
x = noofsubarray(arr,k)
print(x)
y = noofsubarray(arr,k-1)
print(y)
print(x-y)

