# #  solve sudoko 

# def solvesudoko(board):
#     solve(board)

# def solve(board):
#     for i in range(len(board[0])):
#         for j in range(len(board[0])):
#             if board[i][j]  == ".":
#                 for c in map(str,range(1,10)):
#                     if isvalid(board,i,j,c):
#                         board[i][j] = c

#                         if solve(board)==True:
#                             return True
#                         else:
#                             board[i][j] = "."
#                 return False
#     return True

# def isvalid(board,row,col , c):
#     for i in range(0,9):
#         if board[row][i] == c:
#             return False
#         if board[i][col] ==c:
#             return False
#         if board[3*(row//3)+i//3][3*(col//3) + i%3] ==c:
#             return False
#     return True                   



#  optimal approqch 

def solvesudoko(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # print(rows)
    # print(cols)
    # print(boxes)

    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                num = board[i][j]
                b = 3*(i//3) + (j//3)
                rows[i].add(num)
                cols[j].add(num)
                boxes[b].add(num)
    # print(rows)
    # print(cols)
    # print(boxes)
    # findbestcell(board,rows,cols,boxes)
    solve(board,rows,cols,boxes)

def findbestcell(board,rows,cols,boxes):
    best = None
    best_option = None
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                b = (3*(i//3) + j//3)
                # print("b is :" ,b)
                option = [num for num in map(str, range(1,10))
                          if num not in rows[i]
                          if num not in cols[j]
                          if num not in boxes[b]]
                # print(" i is :",i, "and", "j is ",j ,"and","b is : ",b ,"and", option)
                if best is None or len(option) < len(best_option):
                    best = (i,j)
                    best_option = option
                    if len(option) ==1:
                        return best,best_option 
    # print(best,best_option)
    return best,best_option


def solve(board ,rows,cols,boxes):
    cell , option =  findbestcell(board,rows,cols,boxes)
    if not cell:
        return True
    for num in option:
        i,j = cell
        b = 3*(i//3) + (j//3)
        board[i][j] = num
        rows[i].add(num)
        cols[j].add(num)
        boxes[b].add(num)
        if solve(board,rows,cols,boxes):
            return True
        board[i][j] = "."
        rows[i].remove(num)
        cols[j].remove(num)
        boxes[b].remove(num)
    return False






board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]
# print(board)
solvesudoko(board)
for row in board:
    print(' '.join(row))


