# # N queen problem 
# import copy
# def issafe(row,col,board):
#     dupcol = col
#     duprow = row
#     while(row >= 0 and col >=0):
#         if board[row][col] == "Q":return False
#         row -=1
#         col -=1


#     col = dupcol
#     row = duprow

#     while(col >= 0):
#         if board[row][col] == "Q":return False
#         col -=1


#     col = dupcol
#     row = duprow

#     while(row <len(board[0]) and col >= 0):
#         if board[row][col] =="Q": return False
#         row +=1
#         col -=1
#     return True

    

# def solvenqueen(col , board , ans ):
#     if col == len(board[0]):
#         ans.append(copy.deepcopy(board))  # deep copy is used because 
#         # so it means if it board was 1d aray or list then copy would be enough but for 2d onwards deepcopy is needed
#         return 
#     for i in range(len(board[0])):
#         if issafe(i,col ,board) == True:
#             board[i][col] = "Q"
#             solvenqueen(col+1, board , ans)
#             board[i][col] = "."

# n = int(input())
# board = []
# for i in range(n):
#     board.append(["."]*n)
# print(board)
# # board[1][0] = "Q"    # for checking that entire col or row is not gettingg affected 
# # print(board)
# ans =[]
# solvenqueen(0,board,ans)
# print(ans)
# for solution in ans:
#     for row in solution:
#         print(' '.join(row)) # joining the row elements with space
#     print()  # new line 


#  optimal way for getting permutation
import copy
def solveNqueen(col , board,n ,ans,upperdaig,lowerdaig,leftrow):
    if col == n:
        ans.append(copy.deepcopy(board))
        return 
    for i in range(n):
        if (upperdaig[n-1+col-i] == 0 and lowerdaig[i+col] == 0 and leftrow[i] == 0):
            board[i][col] = "Q"
            upperdaig[n-1+col-i] =1
            lowerdaig[i+col] =1
            leftrow[i] = 1
            solveNqueen(col+1,board,n,ans,upperdaig,lowerdaig,leftrow)
            board[i][col] = "."
            upperdaig[n-1+col-i] =0
            lowerdaig[i+col] =0
            leftrow[i] = 0

n = int(input())
board = []
for i in range(n):
    board.append(["."]*n)
print(board)
leftrow = [0]*n
upperdaig = [0]*(2*n-1)
lowerdaig = [0]*(2*n-1)
ans = []
solveNqueen(0,board,n,ans,upperdaig,lowerdaig,leftrow)
for solution in ans:
    for row in solution:
        print(' '.join(row))
    print()
