def solution(array):
    answer = 0
    array = sorted(array)
    a = int((len(array) + 1)/2)
    answer = array[a-1]
    return answer