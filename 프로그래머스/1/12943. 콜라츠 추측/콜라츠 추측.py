def solution(num):
    count = 0
    while True:
        if count != 500:
            if num%2 == 0:
                num /= 2
                count += 1
            else:
                if num == 1:
                    return count
                else:
                    num = (num * 3) + 1
                    count += 1
        else:
            return -1     
        
        