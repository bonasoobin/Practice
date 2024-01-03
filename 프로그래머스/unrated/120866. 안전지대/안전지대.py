import copy
def solution(board):
    b = copy.deepcopy(board)
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                b[i][j] = 2
                if (i-1 >=0) & ((j+1) <len(board)):
                    b[i-1][j+1] = 2
                if (i-1 >=0):
                    b[i-1][j] = 2
                if (i-1 >=0) & ((j-1)>=0):
                    b[i-1][j-1] = 2
                if (j+1) <len(board):
                    b[i][j+1] = 2
                if (j-1 >=0):
                    b[i][j-1] = 2
                if ((i+1) <len(board)) & ((j+1) <len(board)):
                    b[i+1][j+1] = 2
                if ((i+1) <len(board)):
                    b[i+1][j] = 2
                if (j-1 >=0) & ((i+1) <len(board)):
                    b[i+1][j-1] = 2
    for i in range(len(board)):
        for j in range(len(board[i])):                        
            if b[i][j] == 2:
                count += 1
    return (len(board)*len(board))-count
    #return board