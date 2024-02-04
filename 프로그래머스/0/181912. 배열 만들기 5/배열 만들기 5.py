def solution(intStrs, k, s, l):
    a = []
    for i in range(len(intStrs)):
        a.append(intStrs[i][(s):(s+l)])
        
    answer= []
    for i in range(len(a)):
        if int(a[i]) > k:
            answer.append(int(a[i]))
    return answer