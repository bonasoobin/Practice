import itertools
import math
def solution(balls, share):
    return round(math.factorial(balls) // (math.factorial(share) * math.factorial(balls - share)))