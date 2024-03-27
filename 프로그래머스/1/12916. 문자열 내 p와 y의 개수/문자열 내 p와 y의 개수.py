def solution(s):
    p_count = 0
    y_count = 0
    
    for i in range(len(s)):
        if s[i] == 'P' or s[i] == 'p':
            p_count += 1
        elif s[i] == 'Y' or s[i] == 'y':
            y_count += 1
            
    if p_count == y_count:
        return True
    else:
        return False