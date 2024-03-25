def solution(n):
    if n == 0:
        answer = 0
    else:
        answer = 1
    a = 2
    while a <= n:
        if n % a == 0:
            answer += a
        a += 1
    return answer