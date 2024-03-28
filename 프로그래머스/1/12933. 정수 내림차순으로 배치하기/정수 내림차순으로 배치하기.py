def solution(n):
    n = str(n)
    nlist = []
    for i in range(len(n)):
        nlist.append(int(n[i]))
    nlist = sorted(nlist, reverse = True)

    answer = ''
    for i in range(len(n)):
        answer += answer.join(str(nlist[i]))
    return int(answer)