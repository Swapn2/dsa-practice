# #  rotate image or matrix by 90 degree
# def rotate90(matrix):
#     row= len(matrix)
#     col = len(matrix[0])
#     ans = [[0]*col for _ in range(row)]
#     for i in range(row):
#         for j in range(col):
#             ans[j][row-1-i] = matrix[i][j]
#     return ans

#  optimal approach 
def rotate90(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(i+1, row):
            matrix[i][j],matrix[j][i] = matrix[j][i] , matrix[i][j]
    for i in range(row):
        matrix[i].reverse()
    return matrix

    




                    
row = int(input())
col = int(input())
matrix = []
for i in range(row):
    rows = list(map(int, input().split()))
    if len(rows) == col:
        matrix.append(rows)
print(matrix)
print(rotate90(matrix))