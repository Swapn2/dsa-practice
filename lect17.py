# # finding the largest element in the array


# def largest(arr):
#     max_element = arr[0]
#     for i in range(1 ,len(arr)):
#         if arr[i] > max_element:
#             max_element = arr[i]
#     return max_element

# arr = list(map(int, input().split()))
# print(largest(arr))


#  second largest element in the array without sorting

def second_largest(arr):
    largest = arr[0]
    second_largest = None
    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
    return second_largest

arr = list(map(int, input().split()))
print(second_largest(arr))
            