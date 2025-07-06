#  selection sort 

# arr = list(map(int, input().split()))
# print(arr)

# def swap(arr , i ,j):
#     arr[i],arr[j] = arr[j] , arr[i]

# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         mini  = i
#         for j in range(i,len(arr)):
#             if arr[j] < arr[mini]:
#                 mini = j
#         swap(arr,i,mini)
#     return arr

# print(selection_sort(arr))
        
# # #  Bubble Sort 

# def swap(arr , i ,j):
#     arr[i],arr[j] = arr[j] , arr[i]

# arr = list(map(int,input().split()))
# print(arr)

# def bubble_sort(arr):
#     for i in range(len(arr)-1, 0,-1):
#         didswap = 0
#         for j in range(0, i):
#             if arr[j] > arr[j+1]:
#                 swap(arr,j,j+1)
#                 didswapn = 1
#         if didswapn ==0:
#             break
#     return arr

# print(bubble_sort(arr))

# Insertion Sort 

arr = list(map(int, input().split()))
print(arr)

def swap(arr,i,j):
    arr[i], arr[j] = arr[j] , arr[i]

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        didswap = 0
        while(j>0 and arr[j-1] > arr[j]):
            swap(arr,j,j-1)
            didswap = 1
            j -=1
        if didswap == 0:
            break
    return arr

print(insertion_sort(arr))