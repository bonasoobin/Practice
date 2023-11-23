def solution(n): 
    for i in range(1,11):
        answer = 1
        for j in range(1,i+1):
            answer *= j
            if answer == n:
                return i
            elif answer >= n:
                return i-1
            