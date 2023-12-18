def solution(keyinput, board):
    result = [0,0]
    end = (board[0]-1)//2
    end1 = (board[1]-1)//2
    for i in range(len(keyinput)):
        if (keyinput[i] == 'left') & (result[0] > -end) & (result[0] <= end):
            result[0] -= 1
        elif (keyinput[i] == 'right') & (result[0] >= -end) & (result[0] < end):
            result[0] += 1
        elif (keyinput[i] == 'up') & (result[1] >= -end1) & (result[1] < end1):
            result[1] += 1
        elif (keyinput[i] == 'down') & (result[1] > -end1) & (result[1] <= end1):
            result[1] -= 1
    return result
