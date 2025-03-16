def solution(d, budget):
    answer = 0
    sum = 0
    d = sorted(d)
    for i in range(len(d)):
        sum += d[i]
        if sum <= budget:
            answer += 1
    return answer