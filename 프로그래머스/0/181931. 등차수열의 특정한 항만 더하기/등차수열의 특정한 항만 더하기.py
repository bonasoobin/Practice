def solution(a, d, included):
    answer = 0
    num1 = 0
    for i in range(len(included)):
        answer = a + (d * i)
        if included[i]:
            num1 += answer
    
    return num1