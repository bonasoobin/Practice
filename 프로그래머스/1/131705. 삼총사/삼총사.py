from itertools import combinations

def solution(number):
    answer = 0
    nCr = combinations(number, 3)
    nCr = list(nCr)
    
    for i in range(len(nCr)):
        if sum(nCr[i]) == 0:
            answer += 1
    return answer

