def solution(jobs):
    a = 0
    t = 0
    length = len(jobs)
    jobs.sort(key = lambda x: x[1])
    
    while len(jobs) > 0:
        for i in jobs:
            if i[0] <= a:
                jobs.remove(i)
                a += i[1]-1
                t += a - i[0] +1
                break
        a+=1
    return t//length 

