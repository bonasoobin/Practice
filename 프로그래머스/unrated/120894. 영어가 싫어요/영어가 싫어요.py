def solution(numbers):
    n = 0
    answer = ''
    while n < len(numbers):
        if numbers[n:n+3] == 'one':
            answer += '1'
            n = n+3
        if numbers[n:n+3] == 'two':
            answer += '2'
            n = n+3
        if numbers[n:n+5] == 'three':
            answer += '3'
            n = n+5
        if numbers[n:n+4] == 'four':
            answer += '4'
            n = n+4
        if numbers[n:n+4] == 'five':
            answer += '5'
            n = n+4
        if numbers[n:n+3] == 'six':
            answer += '6'
            n = n+3
        if numbers[n:n+5] == 'seven':
            answer += '7'
            n = n+5
        if numbers[n:n+5] == 'eight':
            answer += '8'
            n = n+5
        if numbers[n:n+4] == 'nine':
            answer += '9'
            n = n+4
        if numbers[n:n+4] == 'zero':
            answer += '0'
            n = n+4
    return int(answer)