def solution(i, j, k):
    count = 0
    a = []
    for q in range(i,j+1):
        for e in range(len(str(q))):
            a.append(str(q)[e])
    
    for w in range(len(a)):
        if str(k) == str(a[w]):
            count += 1
    
    return count