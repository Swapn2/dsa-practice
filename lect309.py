
# maximal rectangle

row = int(input())
col = int(input())
matrix = []
for i in range(row):
    rows = list(map(int,input().split()))
    if len(rows) == col:
        matrix.append(rows)
print(matrix)


def lr(arr):
    maxarea = 0
    st = []
    
    for i in range(len(arr)):
        while len(st) != 0 and arr[st[-1]] > arr[i]:
            element = st.pop()
            if len(st) == 0:
                pse = -1
            else:
                pse = st[-1]
            nse = i
            maxarea = max(maxarea, arr[element] * (nse - pse - 1))
        st.append(i)

    # now clear remaining stack
    while len(st) != 0:
        element = st.pop()
        if len(st) == 0:
            pse = -1
        else:
            pse = st[-1]
        nse = len(arr)
        maxarea = max(maxarea, arr[element] * (nse - pse - 1))
    return maxarea


def rectancle(matrix):
    col = len(matrix[0])
    row = len(matrix)
    psum = [[0 for _ in range(col)] for _ in range(row)]
    print(psum)
    maxarea = 0
    for j in range(col):
        sum = 0
        for i in range(row):
            sum += matrix[i][j]
            if matrix[i][j] ==0:
                sum = 0
            psum[i][j] = sum
    print(psum)
    for i in range(row):
        maxarea = max(maxarea, lr(psum[i]))
    return maxarea
            

print(rectancle(matrix))