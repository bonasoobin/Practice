def solution(rny_string):
    a = list(rny_string)
    b = ''
    for i in range(len(a)):
        if a[i] == 'm':
            a[i]='rn'
        b = b+a[i]
    return b