def solution(hp):
    a = 0;b=0;c=0
    a = int(hp/5)
    b = int((hp%5)/3)
    c = int(((hp%5)%3)/1)
    return a +b+c