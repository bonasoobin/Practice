def solution(n):
    a = 0
    if n%2 == 1:
        for i in range(n+1):
            if i%2 == 1:
                a += i
    else:
        for i in range(n+1):
           if i%2 == 0:
                a += i*i
    return a