def solution(numbers, k):
    num = numbers * 1000
    a = 0
    for i in range(k - 1):
        a += 2
    return num[a]