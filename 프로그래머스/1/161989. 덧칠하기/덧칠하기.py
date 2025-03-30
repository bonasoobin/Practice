def solution(n, m, section):
    section.sort()
    answer = 0
    c = 0 

    for s in section:
        if s > c:
            answer += 1
            c = s + m - 1

    return answer