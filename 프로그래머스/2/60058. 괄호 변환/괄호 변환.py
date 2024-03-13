def balanced_index(p):
    count = 0  # 왼쪽 괄호의 개수를 세기 위한 변수
    for i in range(len(p)):  # 문자열 p를 순회
        if p[i] == '(':  # 왼쪽 괄호일 경우
            count += 1  # count를 증가시킴
        else:  # 오른쪽 괄호일 경우
            count -= 1  # count를 감소시킴
        if count == 0:  # 균형잡힌 괄호 문자열인 경우
            return i  # 현재 인덱스 반환

# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0  # 왼쪽 괄호의 개수를 세기 위한 변수
    for i in p:  # 문자열 p를 순회
        if i == '(':  # 왼쪽 괄호일 경우
            count += 1  # count를 증가시킴
        else:  # 오른쪽 괄호일 경우
            if count == 0:  # 왼쪽 괄호가 없는데 오른쪽 괄호가 나오면 쌍이 맞지 않음
                return False  # False 반환
            count -= 1  # count를 감소시킴
    return True  # 균형잡힌 괄호 문자열이면 True 반환

def solution(p):
    answer = ''  # 결과 문자열
    if p == '':  # 주어진 문자열이 빈 문자열인 경우
        return answer  # 빈 문자열 반환
    index = balanced_index(p)  # 균형잡힌 괄호 문자열의 인덱스를 구함
    u = p[:index + 1]  # 균형잡힌 괄호 문자열 u
    v = p[index + 1:]  # 나머지 부분 v
    
    # 올바른 괄호 문자열인 경우
    if check_proper(u):
        answer = u + solution(v)  # v에 대해 재귀적으로 함수를 호출한 결과를 u에 붙여 반환
    
    # 올바른 괄호 문자열이 아닌 경우
    else:
        answer = '('  # '(' 추가
        answer += solution(v)  # v에 대해 재귀적으로 함수를 호출한 결과를 추가
        answer += ')'  # ')' 추가
        u = list(u[1:-1])  # 균형잡힌 괄호 문자열 u의 첫번째와 마지막 문자 제거
        for i in range(len(u)):  # u의 모든 문자에 대해 반복
            if u[i] == '(':  # 왼쪽 괄호일 경우
                u[i] = ')'  # 오른쪽 괄호로 변경
            else:  # 오른쪽 괄호일 경우
                u[i] = '('  # 왼쪽 괄호로 변경
        answer += "".join(u)  # 변경된 u를 문자열로 변환하여 answer에 추가
    return answer  # 결과 반환
    
    
    
