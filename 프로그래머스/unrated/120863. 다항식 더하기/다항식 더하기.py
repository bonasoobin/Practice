def solution(polynomial):
    answer = ''
    a = 0
    b = 0
    term = ''
    for i in range(len(list(polynomial))):
        if list(polynomial)[i] == 'x':
            if term:
                a += int(term)
                term = ''
            else:
                a += 1
        elif list(polynomial)[i].isdigit():
            term += list(polynomial)[i]
        elif term:  
            b += int(term)
            term = ''
    if term: 
        b += int(term)

    if a != 0:
        if a == 1:
            if b != 0:
                answer = 'x' + ' + ' + str(b)
            else:
                answer = 'x'
        else:
            if b != 0:
                answer = str(a) + 'x' + ' + ' + str(b)
            else:
                answer = str(a) + 'x'
    else:
        answer = str(b)

    return answer
