def solution(num_list):
    a = ''
    b = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0 :
            a += ''.join(str(num_list[i]))
        else:
            b += ''.join(str(num_list[i]))
    return int(a) + int(b)