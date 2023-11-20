def solution(num, k):
    num = list(str(num))
    count = 0
    for i in range(len(num)):
        if int(num[i]) == k:
            return i+1
        else:
            count += 1
    if count == len(num):
        return -1