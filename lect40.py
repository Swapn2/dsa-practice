# # #  merge sorted array
def merge_sorted_array(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    arr3 = [0]*(n+m)
    left = 0
    right = 0
    index = 0
    while(left <n and right <m):
        if arr1[left] < arr2[right]:
            arr3[index] = arr1[left]
            index+=1
            left+=1
        else:
            arr3[index] = arr2[right]
            index +=1
            right +=1
    while (left < n):
        arr3[index] = arr1[left]
        index+=1
        left+=1
    while (right < m):
        arr3[index] = arr2[right]
        right+=1
        index+=1
    for i in range(n+m):
        if i<n:
            arr1[i] = arr3[i]
        else:
            arr2[i-n] = arr3[i]
    return arr1,arr2



# #  optimal approach 
# #  1 3 5 7   ||  0 2 6 8 9 
# def merge_sorted_array1(arr1,arr2):
    
#     n = len(arr1)
#     m = len(arr2)
#     left = n-1
#     right = 0
#     print(n)
#     print(left)
#     print(right)
#     print(m)
#     while(right < m and left >0):
#         if arr2[right] < arr1[left]:
#             arr2[right] , arr1[left] = arr1[left] , arr2[right]
#             left-=1
#             right +=1
#         else:
#             break
#     print(arr1)
#     arr1.sort()
#     arr2.sort()
#     print(arr1)
#     return arr1, arr2
arr1 = list(map(int , input().split()))
arr2 = list(map(int , input().split()))
# print(arr1)

print(merge_sorted_array(arr1, arr2))
# print(merge_sorted_array1(arr1, arr2))
