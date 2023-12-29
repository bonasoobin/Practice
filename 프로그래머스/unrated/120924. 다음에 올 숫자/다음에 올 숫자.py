def solution(common):
    answer = 0
    c = []
    b = []
    for i in range(1,len(common)):
        cha = common[i] - common[i-1]
        c.append(cha)
        if common[i-1] !=0:
            bi = common[i] // common[i-1]
            b.append(bi)
    if sum(c)/(len(common)-1) == float(c[0]):
        return common[-1] + c[0]
    elif sum(b)/(len(common)-1) == float(b[0]):
        return common[-1] * b[0]