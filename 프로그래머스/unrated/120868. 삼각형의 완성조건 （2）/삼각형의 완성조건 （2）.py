def solution(sides):
    sides = sorted(sides)
    count = 0
    x = sides[1]-sides[0] + 1
    while (sides[1]-sides[0] < x <= sides[1]):
        count+=1
        x+=1
        
    a = x
    while (a < sides[1]+sides[0]):
        count+=1
        a+=1
    return count