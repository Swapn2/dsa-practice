# # finding the largest element in the array


# def largest(arr):
#     max_element = arr[0]
#     for i in range(1 ,len(arr)):
#         if arr[i] > max_element:
#             max_element = arr[i]
#     return max_element

# arr = list(map(int, input().split()))
# print(largest(arr))


# #  second largest element in the array without sorting

# def second_largest(arr):
#     largest = arr[0]
#     second_largest = None
#     if len(arr) < 2:
#         return None  # Not enough elements
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             second_largest = largest
#             largest = arr[i]
#         elif arr[i] < largest and arr[i] > second_largest:
#             second_largest = arr[i]
#     return second_largest

# arr = list(map(int, input().split()))
# print(second_largest(arr))
            

# #  check if an array is sorted or not

# def is_sorted(arr):
#     for i in range(1,len(arr)):
#         if arr[i-1] <= arr[i]:
#             continue
#         else:
#             return False
#     return True


# arr = list(map(int, input().split()))
# print(is_sorted(arr))


# #  remove duplicates from an unsorted array using set 

# def remove_duplicates(arr):
#     unique = set(arr)
#     return list(unique)


# arr = list(map(int, input().split()))
# print(len(remove_duplicates(arr)))
# print(remove_duplicates(arr))



#  remove duplicates from sorted array using two pointers ( optimal solution )


# def remove_duplivates(arr):
#     if len(arr) ==0:
#         return 0
#     j = 0 
#     for i in range(1, len(arr)):
#         if arr[j] != arr[i]:
#             j+=1
#         arr[j] = arr[i]
#     return j+1

# arr = list(map(int, input().split()))
# print(remove_duplivates(arr))





