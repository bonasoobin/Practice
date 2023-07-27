from functools import reduce

def solution(n):
    answer = reduce((lambda x, y: int(x) + int(y)), str(n), 0)
    return answer