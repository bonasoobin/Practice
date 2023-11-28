n = int(input())

student = []
for _ in range(n):
    a = list(input().split())
    student.append(a)
# 점수는 int형으로 바꿔주기
for i in range(len(student)):
    for j in range(1,4):
        student[i][j] = int(student[i][j])

# 2차원 리스트 정렬하기
student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(len(student)):
    print(student[i][0])
