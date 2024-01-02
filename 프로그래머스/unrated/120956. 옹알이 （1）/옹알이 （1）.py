# from itertools import combinations, permutations

# def solution(babbling):
#     b = ["aya", "ye", "woo", "ma"]
#     c = []
#     for i in range(len(babbling)):
#         a = list(permutations(babbling, i+1))
#         for j in range(len(a)):
#             result = "".join(a[j])
#             c.append(result)
#     bc = []
#     for i in range(len(b)):
#         a = list(permutations(b, i+1))
#         for j in range(len(a)):
#             result = "".join(a[j])
#             bc.append(result)
#     bc = list(set(bc))    
#     c = list(set(c))        

#     count = 0
#     for i in range(len(bc)):
#         for j in range(len(c)):
#             if bc[i] == c[j]:
#                 count += 1
#     return count

def solution(babbling):
    answer = 0
    count = 0
    for b in babbling:
        b = b.replace('aya','1')
        b = b.replace('ye','2')
        b = b.replace('woo','3')
        b = b.replace('ma','4')
        if b.isdigit() == True:
            count += 1


    return count