def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        point = 0
        for j in range(len(name)):
            for k in range(len(photo[i])):
                if photo[i][k] == name[j]:
                    point += yearning[j]
        answer.append(point)
    return answer