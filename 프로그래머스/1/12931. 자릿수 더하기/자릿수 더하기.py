def solution(n):
    a = str(1)
    n = str(n)
    
    for _ in range(len(n)-1):
        a += '0'
    
    answer = 0
    
    while int(a) >= 1:
        answer += int(n) // int(a)
        a = int(a) // 10
        n = str(n[1:])
    return answer