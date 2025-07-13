# better approach


# def set_matrix_zeros(matrix):
#     row = [0]*len(matrix)
#     col = [0]*len(matrix[0])

#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 0:
#                 row[i] = 1
#                 col[i] = 1
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if row[i] ==1 or col[j] ==1:
#                 matrix[i][j] = 0
#     return matrix




#  optimal approach

def set_matrix_zeros(matrix):
    # row  = matrix[..][0]
    # col = matrix[0][..]
    col0 = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] ==0:
                matrix[i][0] = 0
                if j!=0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    for i in range(1, len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j] != 0:
                if matrix[i][0]==0 or matrix [0][j] ==0:
                    matrix[i][j] =0
    if matrix[0][0] == 0:
        for j in range(len(matrix)):
            matrix[0][j] = 0
    if col0 ==0:
        for i in range(len(matrix[0])):
            matrix[i][0] = 0
    return matrix

            





row = int(input())
col = int(input())

matrix = []

for i in range(row):
    rows = list(map(int, input().split()))
    if len(rows) == col:
        matrix.append(rows)
    
print(matrix)

print(set_matrix_zeros(matrix))