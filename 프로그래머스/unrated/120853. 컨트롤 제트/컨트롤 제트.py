def solution(s):
    s = s.split(' ')
    answer = 0
    for i in range(len(s)):
        if i == (len(s)-1):
            if (s[i] != 'Z') & (s[i].lstrip('-').isdigit()):
                answer += int(s[i])
        else:
            if (s[i+1] != 'Z') & (s[i].lstrip('-').isdigit()):
                answer += int(s[i])
    return answer