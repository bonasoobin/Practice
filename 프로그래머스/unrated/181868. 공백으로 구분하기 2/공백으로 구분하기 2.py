def solution(my_string):
    a = []
    answer = my_string.split(' ')
    for i in range(len(answer)):
        if answer[i] != '':
            a.append(answer[i])
    return a