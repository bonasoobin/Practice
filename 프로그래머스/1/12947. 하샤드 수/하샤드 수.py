def solution(x):
    answer = 0
    x = str(x)
    for i in range(len(x)):
        answer += int(x[i])
    if int(x)%answer == 0:
        return True
    else:
        return False