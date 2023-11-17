def solution(age):
    res = []
    num_list = list(map(int, str(age)))
    al = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e',
         5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    for i in range(len(num_list)):
            res.append(al[num_list[i]])
    result = ''.join(res)
    return result