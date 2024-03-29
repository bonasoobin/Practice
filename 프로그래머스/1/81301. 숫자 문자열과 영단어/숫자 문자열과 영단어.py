def solution(s):
    answer = ''
    for i in range(len(s)):
        if s[i].isdigit() == True:
            answer += str(s[i])
        else:
            if s[i:i+3] == 'one':
                answer += str(1)
                i += 3
            elif s[i:i+3] == 'two':
                answer += str(2)
                i += 3
            elif s[i:i+5] == 'three':
                answer += str(3)
                i += 5
            elif s[i:i+4] == 'four':
                answer += str(4)
                i += 4               
            elif s[i:i+4] == 'five':
                answer += str(5)
                i += 4               
            elif s[i:i+3] == 'six':
                answer += str(6)
                i += 3               
            elif s[i:i+5] == 'seven':
                answer += str(7)
                i += 5              
            elif s[i:i+5] == 'eight':
                answer += str(8)
                i += 5              
            elif s[i:i+4] == 'nine':
                answer += str(9)
                i += 4
            elif s[i:i+4] == 'zero':
                answer += str(0)
                i += 4                
    return int(answer)