# def solution(n):
#     answer = 0
#     for i in range(2, n+1):
#         a = 0
#         if i == 2 or i%2 != 0 :
#             for j in range(1, i+1):
#                 if i%j == 0:
#                     a += 1
#             if a == 2:
#                 answer += 1
#     return answer

# 에라토스테네스의 체 
def solution(n):
    prime_nums = set(range(2,n+1))
    
    for i in range(2, int(n**0.5)+1):
        if i in prime_nums:
            prime_nums -= set(range(i*2,n+1,i))
            
    return len(prime_nums)