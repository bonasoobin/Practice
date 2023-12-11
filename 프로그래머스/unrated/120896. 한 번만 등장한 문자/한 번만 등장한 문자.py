def solution(s):
    answer = ''
    s = list(s)
    for i in range(len(s)):
        countt = s.count(s[i])
        if countt == 1:
            answer += s[i]
    answer = sorted(answer)
    result = ''.join(answer)	
    return result