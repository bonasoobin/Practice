def solution(dots):
    answer = 0
    if lk(dots[0],dots[1]) == lk(dots[2],dots[3]):
        answer = 1
    if lk(dots[0],dots[2]) == lk(dots[1],dots[3]):
        answer = 1
    if lk(dots[0],dots[3]) == lk(dots[1],dots[2]):
        answer = 1
    return answer

def lk(dot1,dot2):
    return (dot2[1] - dot1[1] ) / (dot2[0] - dot1[0])