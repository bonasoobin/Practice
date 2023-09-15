def solution(n):
    cnt = 0
    for i in range(1,1001):
        if n == (i * i):
            cnt += 1
    if cnt == 1:
        return 1
    else:
        return 2