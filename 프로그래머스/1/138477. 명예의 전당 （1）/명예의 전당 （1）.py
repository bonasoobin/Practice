def solution(k, score):
    answer = []
    a = []
    for i in range(len(score)):
        if i <= k-1:
            a.append(score[i])
            a = sorted(a)
            answer.append(a[0])
        else:
            if score[i] >= a[0]:
                a.append(score[i])
                a = sorted(a)
                a.remove(a[0])
                answer.append(a[0])
            else:
                answer.append(a[0])
            
    return answer