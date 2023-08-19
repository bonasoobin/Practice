def solution(num_str):
    li = list(num_str)
    result = 0
    for i in range(len(li)):
        result += int(li[i])
    return result