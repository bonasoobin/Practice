def solution(s):
    a = [] # 자를 문자 단위 저장
    for i in range(len(s)):
        a.append(i+1)
        
    
    c = [] # 각 개수별로 잘린 문자열 저장
    
    for i in range(len(a)): # 몇개씩 잘라볼지 정하고 
        b = [] # j개별로 잘린 문자열 저장
        for j in range(len(s)//a[i]): # 실제로 그만큼씩 쪼개기
            strr = s[(a[i]*(j)):(a[i]*(j+1))]
            b.append(strr)
        if (len(s)%a[i]) != 0:
            b.append(s[-(len(s)%a[i]):])
        c.append(b)
    '''
    print(c)
    [['a', 'a', 'b', 'b', 'a', 'c', 'c', 'c'], ['aa', 'bb', 'ac', 'cc'], ['aab', 'bac', 'cc'], 
    ['aabb', 'accc'], ['aabba', 'ccc'], ['aabbac', 'cc'], ['aabbacc', 'c'], ['aabbaccc']]
    '''
    
    d = []
    for i in range(len(c)):
        count = 1
        e = []
        for j in range(len(c[i])):
            if j < (len(c[i])-1):
                if c[i][j] == c[i][j+1]:
                    count += 1
                else:
                    if (j-1) >= 0:
                        f = []
                        
                        if count == 1:
                            count = 1.
                            f.append(str(count))
                            f.append(str(c[i][j]))
                        else:
                            f.append(str(count))
                            f.append(str(c[i][j-1]))
                        count = 1
                        result = ''.join(f)
                        e.append(result)
                    else:
                        f = []
                        f.append(str(c[i][j]))
                        result = ''.join(f)
                        e.append(result)                    
            else:
                f = []
                if count == 1:
                    count = 1.
                    f.append(str(count))
                    f.append(str(c[i][j]))
                    result = ''.join(f)
                    e.append(result)
                else:
                    f.append(str(count))
                    f.append(str(c[i][j]))
                    result = ''.join(f)
                    e.append(result)
        d.append(e)
    
    
    
    h = []
    for i in d:
        g = []
        g.append(''.join(i))
        result = ''.join(g)
        result = result.replace('1.0', '')
        h.append(result)
    
    
    q = []
    for i in range(len(h)):
        q.append(len(h[i]))

    return min(q)