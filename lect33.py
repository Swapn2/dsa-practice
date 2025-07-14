# number of subarrays with sum = k  brute approach
# def n_subarray(arr, k):
#     n = len(arr)
#     count = 0
#     for i in range(n):
#         for j in range(i,n):
#             sum = 0
#             for m in range(i,j+1):
#                 sum = sum +arr[m]
#             if sum == k:
#                 count +=1
#     return count 


# #  number of subarray with sum = k better approach 
# def n_subarray(arr,k):
#     n = len(arr)
#     count = 0
#     for i in range(n):
#         sum = 0 
#         for j in range(i, n):
#             sum = sum +arr[j]
#             if sum ==k:
#                 count +=1
#     return count


# #  number of subarray with sum = k optimal approach 
# def n_subarray(arr,k):
#     hash = {}
#     hash[0] = 1
#     sum = 0
#     count = 0
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#         rem = sum -k
#         if rem in hash:
#             count = count + hash[rem]
#             hash[rem] = hash[rem] +1
#         if sum not in hash:
#             hash[sum] = 1
#     return count

arr= list(map(int, input().split()))
k = int(input())
print(n_subarray(arr,k))