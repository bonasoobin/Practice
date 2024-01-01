def solution(num, total):
    result = []
    if num%2 !=0:
        x = total//num
        result.append(x)
        for i in range(num//2):
            result.append(x-(i+1))
            result.append(x+(i+1))
        result = sorted(result)
        return result
    else:
        x = total/num
        result.append(int(x+0.5))
        result.append(int(x-0.5))
        for i in range((num-2)//2):
            result.append(x-(i+1.5))
            result.append(x+(i+1.5))
        result = sorted(result)
        return result