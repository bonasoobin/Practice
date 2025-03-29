def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True)
    box = []
    a = 0
    for i in range(len(score) // m):
        i = a
        b = []
        c = 0
        while len(b) != m:
            b.append(score[i + c])
            c += 1
            if len(b) >= m:
                break
        a = i + m
        box.append(b)
    for j in range(len(box)):
        answer += (min(box[j]) * m)
    return answer