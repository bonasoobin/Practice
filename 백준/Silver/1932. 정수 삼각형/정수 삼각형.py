n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

triangle_complete = []
for i in range(len(triangle)):
    triangle_ing = []
    if len(triangle[i]) == 1:
        triangle_ing.append(triangle[i][0])
        
    elif len(triangle[i]) == 2:
        triangle_ing.append(triangle_complete[i-1][0] + triangle[i][0])
        triangle_ing.append(triangle_complete[i-1][0] + triangle[i][1])

    else:
        triangle_ing.append(triangle_complete[i-1][0] + triangle[i][0])
        for j in range(1, len(triangle[i])-1):
            triangle_ing.append(max(triangle_complete[i-1][j-1] + triangle[i][j], triangle_complete[i-1][j] + triangle[i][j]))
        triangle_ing.append(triangle_complete[i-1][-1] + triangle[i][-1])
        
    triangle_complete.append(triangle_ing)
    
print(max(triangle_complete[-1]))