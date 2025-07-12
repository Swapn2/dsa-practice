# #  longest consecutive sequence 


# def longest_consecutive_sequence(arr):
#     longest = 1
#     n = len(arr)
#     for i in range(n):
#         x = arr[i]
#         count = 1
#         while (ls(arr, x+1) == True):
#             count +=1
#             x= x+1
#         longest = max(count , longest)
#     return longest
# def ls(arr,num):
#     for i in range(len(arr)):
#         if arr[i] == num:
#             return True
#     return False

# arr = list(map(int, input().split()))
# print(longest_consecutive_sequence(arr))


# # longest consecutive array 
# def longest_consecutive_array(arr):
#     n = len(arr)
#     sorted(arr)
#     longest = 1
#     countcurr = 0
#     last_smaller = int_min
#     for i in range(arr):
#         if (arr[i] -1 == last_smaller):
#             count +=1
#             last_smaller = arr[i]
#         elif arr[i] != last_smaller:
#             count = 1
#             last_smaller = arr[i]
#         longest = max(longest, count)
#     return longest

#  optimal approach 
def longest_consecutive_array(arr):
    longest = 1
    ar = set(arr)
    for i in arr:
        if i-1 not in arr:
            current =i
            count = 1
            while current +1 in arr:
                count +=1
                current +=1
            longest = max(count , longest)
    return longest

arr = list(map(int , input().split()))
print(longest_consecutive_array(arr))

