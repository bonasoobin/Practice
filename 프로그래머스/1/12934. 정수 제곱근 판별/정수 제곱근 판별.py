import math
def solution(n):
    answer = 0
    if math.sqrt(n) == int(math.sqrt(n)):
        return (int(math.sqrt(n))+1) * (int(math.sqrt(n))+1)
    else:
        return -1