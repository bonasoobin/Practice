def solution(n):
    a = 0
    for i in range(n):
        if n % (i+1) == 0:
            a += 1
    return a