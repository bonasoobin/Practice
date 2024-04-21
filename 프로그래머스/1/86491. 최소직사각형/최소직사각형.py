def solution(sizes):
    max_ = []
    min_ = []
    for i in range(len(sizes)):
        max_.append(max(sizes[i][0], sizes[i][1]))
        min_.append(min(sizes[i][0], sizes[i][1]))
    
    a = max(max_)
    b = max(min_)
    
    return a*b