def solution(n):
    answer = []
    while n != 1:
        for i in range(2,n+1):
            if n%i == 0:
                n = n//i
                answer.append(i)
                break
    answer = set(answer)
    answer = sorted(answer)
    return answer