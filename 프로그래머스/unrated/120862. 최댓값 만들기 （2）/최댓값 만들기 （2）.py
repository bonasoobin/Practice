def solution(numbers):
    maax = -10000 * 10000
    for i in range(len(numbers)):
        for j in range(1,len(numbers)):
            if i != j:
                if maax < (numbers[i] * numbers[j]):
                    maax = (numbers[i] * numbers[j])
    return maax