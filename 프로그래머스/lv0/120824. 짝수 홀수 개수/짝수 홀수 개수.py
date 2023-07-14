def solution(num_list):
    answer = []
    a = b = 0
    for n in range(len(num_list)):
        if num_list[n] % 2 == 0:
            a += 1
        else:
            b += 1
    answer = [a,b]
    return answer