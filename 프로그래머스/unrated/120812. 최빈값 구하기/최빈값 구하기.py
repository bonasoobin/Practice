import statistics

def solution(array):
    a = []
    for i in range(len(array)):
        a.append(array[-(i+1)])
        
    b = statistics.mode(array)
    c = statistics.mode(a)
    if b==c:
        return b
    else:
        return -1
    