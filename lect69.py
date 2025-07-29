#  search in the 2D matrix 

# brute approach 
# def search(matrix , target):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if target == matrix[i][j]:
#                 return True 
#     return False


# better approach   


# def bs(arr,k):
#     n = len(matrix)
#     low = 0
#     high = n
#     while(low <= high):
#         mid = (low+high)//2
#         if arr[mid] == k:
#             return True
#         elif arr[mid] < k:
#             low = mid+1
#         else:
#             high = mid -1


# def search(matrix, target):
#     for i in range(len(matrix)):
#         if matrix[i][0] <= target and matrix[i][len(matrix[0])-1] >= target:
#             return bs(matrix[i],target)


# optimal approach 


def search(matrix,target):
    row = len(matrix)
    col = len(matrix[0])
    low = 0
    high = (row*col)-1
    while(low <= high):
        mid = (low+high)//2
        r = mid//col
        c = mid%col
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            low = mid+1
        else:
            high = mid+1
    return False


row = int(input())
col = int(input())

matrix =[]
for i in range(row):
    rows = list(map(int, input().split()))
    if len(rows) == col:
        matrix.append(rows)
print(matrix)
target = int(input())
print(search(matrix,target))



