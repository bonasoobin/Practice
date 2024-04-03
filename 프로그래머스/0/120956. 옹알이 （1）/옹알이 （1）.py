def solution(babbling):
    answer = 0
    count = 0
    for b in babbling:
        b = b.replace('aya','1')
        b = b.replace('ye','2')
        b = b.replace('woo','3')
        b = b.replace('ma','4')
        if b.isdigit() == True:
            count += 1


    return count