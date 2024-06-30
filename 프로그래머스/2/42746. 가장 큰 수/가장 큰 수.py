from functools import cmp_to_key

def compare(x, y):
    # 두 문자열을 결합하여 비교
    if x + y > y + x:
        return -1  # x + y가 더 크면 x를 앞에 배치
    elif x + y < y + x:
        return 1   # y + x가 더 크면 y를 앞에 배치
    else:
        return 0   # x + y와 y + x가 같으면 순서를 유지

def solution(numbers):
    # 숫자를 문자열로 변환
    str_numbers = list(map(str, numbers))
    
    # 비교 함수를 key 함수로 변환
    key_func = cmp_to_key(compare)
    
    # 정렬 알고리즘을 사용하여 정렬
    str_numbers.sort(key=key_func)
    
    # 정렬된 숫자를 하나의 문자열로 합침
    result = ''.join(str_numbers)
    
    # 결과가 '0'으로 시작하는 경우 (모두 0인 경우) '0' 반환
    if result[0] == '0':
        return '0'
    return result