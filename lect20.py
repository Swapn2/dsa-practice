# #  longest subarray with sum = K , positive numbers are there in array 
# def longest_subarray_with_sum_k(arr, k):
#     length =0
#     for i in range(len(arr)):

#         for j in range(i,len(arr)):
#             sum = 0
#             for m in range(i, j+1):
#                 sum = sum+ arr[m]
#             if sum == k:
#                 length = max(length, j-i+1)
#     return length

# arr = list(map(int, input().split()))
# k = int(input())
# print(longest_subarray_with_sum_k(arr, k)) 

# # lets do it  in n square 

# def longest_subarray_with_sum_k(arr, k):
#     length =0
#     for i in range(len(arr)):
#         sum = 0
#         for j in range(i,len(arr)):
#             sum = sum+ arr[j]
#             if sum == k:
#                 length = max(length, j-i+1)
#     return length

# arr = list(map(int, input().split()))
# k = int(input())
# print(longest_subarray_with_sum_k(arr, k)) 

# #  better approach using dictionary

# def longest_subarray_with_sum_k(arr, k):
#     hash = {}
#     sum = 0 
#     max_len = 0
#     for i in range(len(arr)):
#         sum +=arr[i]
#         if sum == k:
#             max_len = max(max_len, i+1)
#         rem = sum -k

#         if rem in hash:
#             length = i - hash[rem]
#             max_len = max(max_len, length)
        
#         if sum not in hash:
#             hash[sum] = i
#     return max_len

# arr = list(map(int, input().split()))
# k = int(input())
# print(longest_subarray_with_sum_k(arr, k))

#  optimal approach using 2 pointers

def longest_subarray_with_sum_k(arr, k):
    left = 0
    sum = arr[0]
    max_len = 0
    right = 0
    while (right < len(arr)):
        right +=1 
        if right <len(arr):
            sum +=arr[right]
        if sum ==k:
            max_len = max(max_len , right-left +1)
        while (sum >k and left < right ):
            sum -=arr[left]
            left+=1 
    return max_len

arr = list(map(int, input().split()))
k = int(input())
print(longest_subarray_with_sum_k(arr, k))