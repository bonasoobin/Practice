def solution(my_string, m, c):
    answer = []
    for i in range(len(my_string)):
        if i % m == c-1:
            answer.append(my_string[i])
    a = ''.join(answer)
    return a