def solution(num_list, n):
    result = []
    answer = []
    for i in range(len(num_list)):
        if i%n != (n-1):
            result.append(num_list[i])
        else:
            result.append(num_list[i])
            answer.append(result)
            result = []
    return answer