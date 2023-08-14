import math
def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    elif len(num_list) <= 10:
        return math.prod(num_list)