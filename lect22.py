#  sort array of 0s , 1s and 2s

# def sort012(arr):
#     count0 = 0
#     count1 = 0
#     count2 = 0

#     for i in range(len(arr)):
#         if arr[i] == 0:
#             count0 +=1
#         elif arr[i] == 1:
#             count1 +=1
#         else:
#             count2 +=1
#     print(count0)
#     print(count1)
#     print(count2)
#     for i in range(count0):
#         arr[i] = 0
#     for i in range(count0 , count0+count1):
#         arr[i] = 1
#     for i in range(count0+count1, count0+count1+count2):
#         arr[i] = 2
#     return arr
# arr = list(map(int, input().split()))
# print(sort012(arr))

# #  dutch national Flag algorithm 

# def sort012(arr):
#     low = 0 
#     mid = 0
#     high = len(arr)-1 
#     while mid <= high:
#         if arr[mid] == 0:
#             arr[low] , arr[mid] = arr[mid] , arr[low]
#             low +=1 
#             mid +=1 
#         elif arr[mid] == 1:
#             mid +=1 
#         elif arr[mid] == 2:
#             arr[mid] , arr[high] = arr[high] , arr[mid]
#             high -= 1 
#     print(low)
#     print(mid)
#     print(high)
#     return arr

# arr = list(map(int , input().split()))
# print(sort012(arr)) 

