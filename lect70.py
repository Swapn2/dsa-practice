#  search in 2d array matrix is not entirely sorted , 
# row wise sorted and column wise sorted

def search(matrix,target):
    row = 0 
    col = len(matrix[0])-1
    while(row < len(matrix) and col >= 0):
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row +=1
        else:
            col -=1
    return False




row = int(input())
col = int(input())
matrix = []
for i in range(row):
    rows = list(map(int,input().split()))
    if len(rows) == col:
        matrix.append(rows)
print(matrix)
target = int(input())
print(search(matrix,target))