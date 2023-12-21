def solution(score):
    meann = []
    for i in range(len(score)):
        a = (score[i][0] + score[i][1])/2
        meann.append(a)
    a = meann.index
    rank = [sorted(meann, reverse=True).index(i)+1 for i in meann]
    return rank