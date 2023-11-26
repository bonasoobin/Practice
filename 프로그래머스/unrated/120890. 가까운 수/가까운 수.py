def solution(array, n):
    a = []
    for i in range(len(array)):
        a.append(abs(array[i] - n))
    
    b = min(a)
    count = []
    for i in range(len(a)):
        if a[i] == b:
            count.append(i)
    
    if len(count) == 1:
        return array[count[0]]
    else:
        answer = 100
        for i in range(len(count)):
            if array[count[i]] < answer:
                answer = array[count[i]]
        return answer