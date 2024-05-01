def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    
    new_reserve = [r for r in reserve if r not in lost] # reserve 중에서 lost가 아닌 경우
    new_lost = [l for l in lost if l not in reserve] # lost 중에서 reserve가 아닌 경우
    
    for i in range(len(new_reserve)):
        a = new_reserve[i] - 1 # 앞번호 학생 확인
        b = new_reserve[i] + 1 # 뒷번호 학생 확인
        
        if a in new_lost:
            new_lost.remove(a)
        elif b in new_lost:
            new_lost.remove(b)
            
    return n - len(new_lost)