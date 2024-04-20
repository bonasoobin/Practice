# def solution(scoville, K):
#     answer = 0
    
#     while True:
#         count = 0
#         for i in range(len(scoville)):
#             if scoville[i] < K:
#                 count += 1
#         if count == 0:
#             return answer
#             break
#         elif len(scoville) == 1:
#             return -1
#             break
        
#         s = []
#         scoville = sorted(scoville)
#         s.append(scoville[0] + (scoville[1]*2))
#         s += scoville[2:]
#         scoville = s
#         answer += 1


import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        new = a + (b*2)
        
        heapq.heappush(scoville, new)
        
        answer += 1
    
    return answer