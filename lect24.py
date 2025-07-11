# # #  sum of maximum subarray using  kadane's 
# def subarraysum(arr):
#     sum = 0
#     int_maxi = arr[0]
#     start = 0
#     end = 0
#     for i in range(len(arr)):
#         if sum == 0: start = i
#         sum = sum+arr[i]
#         int_maxi = max(sum,int_maxi)
#         end = i

#         if sum < 0:
#             sum =0
#     return int_maxi

# arr = list(map(int, input().split()))
# print(subarraysum(arr))



 
# # #  sum of maximum subarray using  kadane's printing array too

# def subarraysum(arr):
#     sum = 0
#     int_maxi = arr[0]
#     start = 0
#     end = 0
#     for i in range(len(arr)):
#         if sum == 0: start = i
#         sum = sum+arr[i]
#         int_maxi = max(sum,int_maxi)
#         end = i

#         if sum < 0:
#             sum =0
#     for i in range(start , end +1):
#         print(arr[i],end = " ")

# arr = list(map(int, input().split()))
# print(subarraysum(arr))



 