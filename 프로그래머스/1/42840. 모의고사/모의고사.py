def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    count_a = count_b = count_c = 0
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            count_a += 1
        if answers[i] == b[i % len(b)]:
            count_b += 1
        if answers[i] == c[i % len(c)]:
            count_c += 1
    
    answer = []
    max_count = max(count_a, count_b, count_c)
    if count_a == max_count:
        answer.append(1)
    if count_b == max_count:
        answer.append(2)
    if count_c == max_count:
        answer.append(3)
        
    return answer
        
    