#  spiral matrix traversal 

def spiral(arr):
    row = len(arr)
    col = len(arr[0])
    ans = []
    top = 0
    left =0 
    bottom = row-1
    right = col-1
    while(top <= bottom and left <= right):
        for i in range(left, right+1):
            ans.append(arr[top][i])
        top+=1
        if top <= bottom:
            for i in range(top , bottom+1):
                ans.append(arr[i][right])
        right -=1
        if left <= right:
            for i in range(right , left-1,-1):
                ans.append(arr[bottom][i])
        bottom -=1
        if top <= bottom and left <= right:
            for i in range(bottom,top-1, -1):
                ans.append(arr[i][left])
        left +=1
    return ans


row = int(input())
col = int(input())
matrix = []
for i in range(row):
    rows = list(map(int, input().split()))
    if len(rows) == col:
        matrix.append(rows)
print(matrix)
print(spiral(matrix))