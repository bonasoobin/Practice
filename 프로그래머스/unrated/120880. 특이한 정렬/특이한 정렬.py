def solution(numlist, n):
    return sorted(numlist, key = lambda a : (abs(n-a),n-a))