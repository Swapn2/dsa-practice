# #  missing number in an array of n-1 integers from 1 to n

# def missing_number(arr):
#     for i in range(1 , max(arr)+1):
#         flag = 0
#         for j in range(len(arr)):
#             if arr[j] == i:
#                 flag = 1
#                 break
#         if flag == 0:
#             return i
        
# arr = list(map(int, input().split()))
# print(missing_number(arr))

# # #  missing number in an array of n-1 integers from 1 to n better approach

# def missing_number(arr):
#     hash = [0]*(max(arr)+1)
#     for i in range(len(arr)):
#         hash[arr[i]] = 1
#     for i in range(1,len(hash)):
#         if hash[i] == 0:
#             return i
        
        
# arr = list(map(int, input().split()))
# print(missing_number(arr))

# # #  missing number in an array of n-1 integers from 1 to n optimal approach

# def missing_number(arr):
#     s2 = 0
#     sum = max(arr)*(max(arr)+1)//2
#     for i in range(len(arr)):
#         s2 += arr[i]
#     return sum - s2

# arr = list(map(int, input().split()))
# print(missing_number(arr))

# #  missing number in an array of n integers from 0 to n optimal approach using XOR

# def missing_number(arr):
#     n = len(arr)
#     xor1 = 0
#     xor2 = 0
#     for i in range(n):
#         # print(i, end='\n')
#         xor2 ^= i+1
#         xor1 ^= arr[i]
#     return xor1^xor2

# arr = list(map(int, input().split()))
# print(missing_number(arr))

# #  coutn maximum consecutive 1's in a binary array optimal approach 

# def max_consecutive_ones(arr):
#     count = 0
#     maxi = 0 
#     for i in range(len(arr)):
#         if arr[i] == 1 :
#             count +=1 
#             maxi = max(count , maxi)
#         else:
#             count = 0
#     return maxi

# arr = list(map(int, input().split()))
# print(max_consecutive_ones(arr))

# # find the number that appears only once in an array where every other number appears twice 
# # XOR approach

# def find_unique(arr):
#     xor = 0
#     for i in range(len(arr)):
#         xor ^= arr[i]
#     return xor
# arr = list(map(int, input().split()))
# print(find_unique(arr))