def solution(numbers):
    sum = 0
    for a in range(len(numbers)):
        sum += numbers[a]
        answer = sum / len(numbers)
    return answer