# #  left rotate by 1 place 

# def left_rotate(arr):
#     first = arr[0]
#     for i in range(1, len(arr)):
#         arr[i-1] = arr[i]
#     arr[-1] = first
#     return arr

# arr = list(map(int, input().split()))
# print(arr)
# print(left_rotate(arr))


# #  left rotate by d place 

# def left_rotate(arr,d):
#     d = d%len(arr)
#     temp = [0]*d

#     for i in range(0,d):
#         temp[i] = arr[i]
#     for i in range(d, len(arr)):
#         arr[i- d] = arr[i]
#     for i in range(0,d):
#         arr[len(arr)-d+i] = temp[i]
#     return arr

# arr = list(map(int , input().split()))
# n = int(input())
# print(arr)
# print(left_rotate(arr, n))



# # #  left rotate by d place  optimal approach 
# def reverse(arr , start , end):
#     while (start < end):
#         arr[start] , arr[end] = arr[end] , arr[start]
#         start +=1 
#         end -=1
#     return arr

# def left_rotate(arr, d):
#     d = d % len(arr)
#     reverse(arr, 0 , d-1)
#     reverse(arr, d , len(arr)-1)
#     reverse(arr, 0 , len(arr)-1)
#     return arr

# arr = list(map(int, input().split()))
# n = int(input())   
# print(arr)
# print(left_rotate(arr, n))


# #  move all zeroes to the end of the array

# def move_zero(arr):
#     temp = [0]*len(arr)
#     j = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             temp[j] = arr[i]
#             j +=1
#     return temp

# arr = list(map(int, input().split()))
# print(arr) 
# print(move_zero(arr))


# #  move all zeroes to the end of the array optimal approach

# def move_zero(arr):
#     j = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[j] = arr[i]
#             j+=1
#     for i in range(j , len(arr)):
#         arr[i] = 0
#     return arr

# arr = list(map(int, input().split()))
# print(arr)
# print(move_zero(arr))


# #  union of two sorted arrays using 

# def union(arr1, arr2):
#     union_set = set()

#     for num in arr1:
#         union_set.add(num)
#     for num in arr2:
#         union_set.add(num)
#     union_set = sorted(union_set)
#     return list(union_set)

# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))  
# print(union(arr1, arr2))


# #  union  of two sorted arrays using two pointers optimal approach

# def union(arr1 , arr2):
#     i = 0
#     j = 0
#     unionarr = []
#     while (i < len(arr1) and j < len(arr2)):
#         if arr1[i] <= arr2[j]:
#             if not unionarr or unionarr[-1] != arr1[i]:
#                 unionarr.append(arr1[i])
#             i += 1
#         elif arr1[i] >= arr2[j]:
#             if not unionarr or unionarr[-1] != arr2[j]:
#                 unionarr.append(arr2[j])
#             j += 1
#     while (i < len(arr1)):
#         if not unionarr or unionarr[-1] != arr1[i]:
#             unionarr.append(arr1[i])
#         i += 1
#     while(j < len(arr2)):
#         if not unionarr or unionarr[-1] != arr2[j]:
#             unionarr.append(arr2[j])
#         j += 1
#     return unionarr

# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))  
# print(union(arr1, arr2))
 

# # #  intersection of two sorted arrays using visited 


# def intersection(arr1 , arr2):
#     n1 = len(arr1)
#     n2 = len(arr2)
#     visited = [0]*max(n1,n2)
#     ans = []
#     for i in range(n1):
#         for j in range(n2):
#             if arr1[i] == arr2[j] and visited[j] == 0:
#                 ans.append(arr1[i])
#                 visited[j] = 1
#                 break
#             if arr1[i] < arr2[j]:
#                 break
#     return ans

# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# print(intersection(arr1, arr2))



# #  intersection of two sorted arrays using two pointers optimal approach

# def intersection(arr1, arr2):
#     i = 0
#     j = 0 
#     ans = []
#     while (i < len(arr1) and j < len(arr2)):
#         if arr1[i] < arr2[j]:
#             i +=1 
#         elif arr2[j] < arr2[j]:
#             j +=1
#         else:
#             ans.append(arr1[i])
#             i+=1
#             j+=1
#     return ans

# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# print(intersection(arr1, arr2))


