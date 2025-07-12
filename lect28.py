# # leaders of an array

# def leader(arr):
#     n = len(arr)
#     ans =[]
#     for i in range(n):
#         flag = True
#         for j in range(i , n):
#             if arr[j] > arr[i]:
#                 flag = False
#                 break
#         if flag == True:
#             ans.append(arr[i])
#     return ans

# arr = list(map(int , input().split()))
# print(leader(arr))


# #  optimal approach

# def leader(arr):
#     int_max = arr[-1]
#     n = len(arr)
#     ans = []

#     for i in range(n-1,-1, -1):
#         if arr[i] >= int_max:
#             int_max = max(int_max , arr[i])
#             ans.append(int_max)
#     return ans

# arr = list(map(int , input().split()))
# print(leader(arr))
