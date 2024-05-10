T = int(input())
t = []


for _ in range(T):
    a = list(map(int, input().split()))
    t.append(a)

for i in range(len(t)):
    answer = 0
    for j in range(len(t[0])):
        if t[i][j] % 2 == 1:
            answer += t[i][j]
    print('#' + str(i+1) + ' ' + str(answer))