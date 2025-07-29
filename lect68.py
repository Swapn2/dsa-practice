#  find the row with maximum number of 1s sorted 

# def maxones(matrix):
#     maxcount = -1
#     index = -1
#     for i in range(len(matrix)):
#         countone = 0
#         for j in range(len(matrix[0])):
#             countone += matrix[i][j]
#         if countone > maxcount:
#             maxcount = countone
#             index = i
#    return index 

#  optimal approach 

def maxones(matrix):
    maxcount = -1
    index = -1
    for i in range(len(matrix)):
        countone = 0
        low = 0
        high = len(matrix[0])-1
        while(low <= high):
            mid = (low+high)//2
            if matrix[i][mid] ==1:
                countone = len(matrix[0]) - mid
                high = mid -1
            else:
                low = mid +1
        if maxcount < countone:
            maxcount = countone
            index = i
    if countone != 0:
        return index
    else:
        return -1


row = int(input())
col = int(input())
matrix = []
for i in range(row):
    rows = list(map(int,input().split()))
    if len(rows) == col:
        matrix.append(rows)
print(matrix)
print(maxones(matrix))