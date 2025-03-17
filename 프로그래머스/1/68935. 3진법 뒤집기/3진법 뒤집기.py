def solution(n):
    answer = 0
    t = ''
    while n > 0:
        t += str(n%3)
        n = n//3
    return int(t,3)
