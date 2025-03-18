def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] != ' ':
            if s[i].islower() == True:
                if ord(s[i]) + n > 122:
                    a = chr(ord(s[i]) + n - 26)
                    answer += answer.join(a)
                else:
                    a = chr(ord(s[i]) + n)
                    answer += answer.join(a)
            elif s[i].islower() == False:
                if ord(s[i]) + n > 90:
                    a = chr(ord(s[i]) + n - 26)
                    answer += answer.join(a)
                else:
                    a = chr(ord(s[i]) + n)
                    answer += answer.join(a)
        else:
            answer += answer.join(' ')
    return answer