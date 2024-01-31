n = list(input())

# 입력 조건 안써도 일단 .. 백준 통과는 됨       

# 몇자리씩 쪼갤지
half = len(n) // 2

# 각 자릿수 양쪽에 더하기
left = 0
right = 0
for i in range(half):
    left += int(n[i])
    right += int(n[half+i])

# 만약 같다면 럭키 출력, 그렇지 않다면 레디 출력
if left == right:
    print('LUCKY')
else:
    print('READY')