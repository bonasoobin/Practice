def solution(x, n):
    answer = []
    while len(answer) != n:
        if len(answer) == 0:
            answer.append(x)
        else:
            answer.append(answer[-1] + x)
    return answer