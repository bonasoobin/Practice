import itertools
def solution(spell, dic):
    answer = []
    nPr = itertools.permutations(spell, len(spell))
    for p in nPr:
        result = "".join(p)
        answer.append(result)
    count = 0
    for i in range(len(answer)):
        for j in range(len(dic)):
            if answer[i] == dic[j]:
                count += 1
    if count >= 1:
        return 1
    else:
        return 2