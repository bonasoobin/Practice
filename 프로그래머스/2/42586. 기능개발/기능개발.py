from math import ceil
from queue import deque


def solution(progresses, speeds):
    long_day = 0
    answer = []
    days = deque(ceil((100 - p) / s) for p, s in zip(progresses, speeds))
    while days:
        day = days.popleft()
        if day > long_day:
            answer.append(1)
            long_day = day
        else:
            answer[-1] += 1
    return answer