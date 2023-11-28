# 정답
n = int(input())
home = list(map(int, input().split()))

home.sort()
# 중간값이 가장 효율적인 곳이니까 중앙값 구하기..
print(home[(n-1)//2])
