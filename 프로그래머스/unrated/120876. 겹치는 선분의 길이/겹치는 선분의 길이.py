# def solution(lines):
#     count = 0
#     lines = sorted(lines)
#     a = []
#     if (lines[1][0] > lines[0][0]) & (lines[1][0] < lines[0][1]):
#         count += (lines[0][1] - lines[1][0]) 
#         #lines[1][0] = lines[0][1]
#         a.append(max(lines[0][0], lines[1][0], lines[2][0]))
#         a.append(min(lines[0][1], lines[1][1], lines[2][1]))
#         #a = [lines[1][0], lines[0][1]]
#     if (lines[1][0] < lines[2][0]) & (lines[2][0] < lines[1][1]):
#         count += (lines[1][1] - lines[2][0])
#     if a != []:
#         if (lines[2][0] <= a[1]) & (a[1] <= lines[2][1]):
#             count -= (abs(a[0]-a[1])) + 1
#     return lines


def solution(lines):
    answer = 0
    line1 = set(range(lines[0][0], lines[0][1]))
    line2 = set(range(lines[1][0], lines[1][1]))
    line3 = set(range(lines[2][0], lines[2][1]))

    answer = sorted(list(line1 & line2 | line1 & line3 | line2 & line3))

    return len(answer)
