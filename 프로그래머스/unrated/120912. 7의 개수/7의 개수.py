def solution(array):
    answer = ''
    for i in range(len(array)):
        answer += str(array[i])
    count = 0
    for i in range(len(answer)):
        if answer[i] == '7':
            count += 1
    return count