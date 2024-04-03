def solution(n):
    if n == 1:
        return [[1]]

    
    answer = [[0] * n for _ in range(n)]
    
    x = 0
    y = 0
    
    direction = 'right'
    
    for i in range(n*n):
        
        answer[x][y] = i+1
        
        if direction == 'right':
            y += 1
            if (y == n-1) or (answer[x][y+1] != 0):
                direction = 'down'
                
        elif direction == 'down':
            x += 1
            if (x == n-1) or (answer[x+1][y] != 0):
                direction = 'left'
        
        elif direction == 'left':
            y -= 1
            if (answer[x][y-1] != 0):
                direction = 'up'
        
        elif direction == 'up':
            x -= 1
            if (answer[x-1][y] != 0):
                direction = 'right'
            
            
            
    return answer