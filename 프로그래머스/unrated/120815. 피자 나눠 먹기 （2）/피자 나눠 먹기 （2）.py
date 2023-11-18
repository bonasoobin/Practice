def solution(n):
    answer = 1
    for answer in range(1,100):
        if (answer*6) % n == 0:
            return answer
