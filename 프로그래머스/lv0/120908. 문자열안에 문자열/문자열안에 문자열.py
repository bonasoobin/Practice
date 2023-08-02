import re

def solution(str1, str2):
    answer = 0
    x = re.findall(str2, str1)
    if len(x) == 0:
        return 2
    else:
        return 1