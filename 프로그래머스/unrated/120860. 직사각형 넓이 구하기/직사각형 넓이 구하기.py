def solution(dots):
    x = 0
    y = 0
    for i in range(len(dots)-1):
        if x < abs(dots[i][0] - dots[i+1][0]):
            x = abs(dots[i][0] - dots[i+1][0])
        if y < abs(dots[i][1] - dots[i+1][1]):
            y = abs(dots[i][1] - dots[i+1][1])
    return x*y