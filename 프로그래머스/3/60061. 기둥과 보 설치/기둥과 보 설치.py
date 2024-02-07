def possible(answer):
    for x, y, ki_or_bo in answer:
        if ki_or_bo == 0: # 기둥을 설치한다고 할때
            # 바닥이거나 기둥 출발점이거나, 보의 한쪽 끝부분 위라면 가능 
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        elif ki_or_bo == 1: # 보를 설치한다고 할때
            # 기둥 출발점이거나, 보를 설치했을때 기둥이랑 연결되거나, 왼쪽점과 오른쪽점에 보가 세워졌으면 가능
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True
            
            
def solution(n, build_frame):
    answer = []
    for i in range(len(build_frame)):
        x, y, ki_or_bo, plus_or_minus = build_frame[i]
        if plus_or_minus == 0: # 삭제라면
            answer.remove([x, y, ki_or_bo]) # 일단 삭제해보고
            if possible(answer) == False: # 불가능하다고 나오면
                answer.append([x, y, ki_or_bo]) # 다시 추가해주기
        if plus_or_minus == 1: # 추가라면
            answer.append([x, y, ki_or_bo]) # 일단 추가해보고
            if possible(answer) == False: # 불가능하다고 나오면
                answer.remove([x, y, ki_or_bo]) # 다시 삭제해주기
    return sorted(answer)