def solution(arr1, arr2):
    answer1 = 0
    answer2 = 0
    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2):
        return 1
    elif len(arr1) == len(arr2):
        for i in range(len(arr1)):
            answer1 += arr1[i]
        for j in range(len(arr2)):
            answer2 += arr2[j]
    
        if answer1 < answer2:
            return -1
        elif answer1 > answer2:
            return 1
        else:
            return 0