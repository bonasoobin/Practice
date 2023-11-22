def solution(n):
    b = 0
    for i in range(1,n+1):
        a = 0
        for j in range(1,i+1):
            if i%j == 0:
                a+=1
        if a>=3:
            b += 1
    return b
            