import re

def solution(my_string):
    answer = 0
    x = re.findall('[0-9]', my_string)
    for i in range(len(x)):
        answer += int(x[i])
    return answer