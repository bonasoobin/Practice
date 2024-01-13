def solution(n):
    answer = []
    for i in range(n):
        a = []
        for j in range(n):
            if i == j:
                a.append(1)
            else:
                a.append(0)
        answer.append(a)
    return answer