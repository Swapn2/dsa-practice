#  # Two Sum Problem (Reading)


# def twosum(arr, sum):
#     for i in range(len(arr)):
#         a = arr[i]
#         for j in range(i+1, len(arr)):
#             b = arr[j]
#             if a + b == sum:
#                 return True
#     return False

# arr = list(map(int, input().split()))
# sum = int(input())
# print(twosum(arr, sum))

# #  # optimal approach using hashing
# def twosum(arr, sum):
#     hash = {}
#     for i in range(len(arr)):
#         a = arr[i]
#         if sum -a in hash:
#             return True
#         hash[a] = i
#     return False 

# arr = list(map(int, input().split()))
# sum = int(input())
# print(twosum(arr, sum))


# # #  dont allow to use map , then we can tell True False by greedy approach 
# def twosum(arr, sum):
#     arr.sort()
#     print(arr)
#     left = 0
#     right = len(arr)-1 
#     while(left < right ):
#         if arr[left] + arr[right] == sum:
#             return True
#         elif arr[left] + arr[right] <  sum:
#             left +=1 
#         else:
#             right -=1 
#     return False

# arr = list(map(int, input().split()))
# sum = int(input())
# print(twosum(arr, sum))