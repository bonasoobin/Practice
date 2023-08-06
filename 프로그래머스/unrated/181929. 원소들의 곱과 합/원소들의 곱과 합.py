def solution(num_list):
    a = 0
    b = 1
    for i in range(len(num_list)):
        a += num_list[i]
        b *= num_list[i]
    if b < (a*a):
        return 1
    elif b > (a*a):
        return 0