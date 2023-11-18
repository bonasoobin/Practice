def solution(order):
    answer = 0
    order = list(str(order))
    for i in range(len(order)):
        order[i] = int(order[i])
        if order[i] % 3 == 0:
            answer += 1
        if order[i]  == 0:
            answer -= 1
    return answer