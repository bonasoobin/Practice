def solution(money):
    answer = []
    a = int(money / 5500)
    b= money%5500
    answer = [a,b]
    return answer