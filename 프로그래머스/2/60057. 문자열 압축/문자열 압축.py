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
            # 마지막에 범위오류 생기지 않도록 if문 지정
            if j < (len(c[i])-1):
                # 만약 지금꺼랑 다음꺼랑 같다면 count += 1
                if c[i][j] == c[i][j+1]:
                    count += 1
                else:
                    # 지금꺼랑 다음꺼랑 같지 않은데 j=0이 아닐때
                    if (j-1) >= 0:
                        f = []
                        # count가 1이라면 count = 1.로 지정해주기(나중에 1 없앨건데 10의 1이 지워지지않게)
                        if count == 1:
                            count = 1.
                            f.append(str(count))
                            f.append(str(c[i][j]))
                        # count가 1이 아니라면 그대로
                        else:
                            f.append(str(count))
                            f.append(str(c[i][j-1]))
                        count = 1
                        result = ''.join(f)
                        e.append(result)
                    # 지금꺼랑 다음꺼랑 같지 않은데 j=0일때 (count=1일수밖에없음(처음이니까) -> 그냥 지금꺼 추가해주기)
                    else:
                        f = []
                        f.append(str(c[i][j]))
                        result = ''.join(f)
                        e.append(result)                    
            # 마지막꺼일때
            else:
                f = []
                # 위와 같은 방식으로 count=1이면 1.로 바꿔주고 아니라면 그대로 추가해주기
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
    '''    
    print(d)
    [['2a', '2b', '1.0a', '3c'], ['aa', '1.0bb', '1.0ac', '1.0cc'], ['aab', '1.0bac', '1.0cc'], 
    ['aabb', '1.0accc'], ['aabba', '1.0ccc'], ['aabbac', '1.0cc'], ['aabbacc', '1.0c'], ['1.0aabbaccc']]
    '''
    
    # 1.0이 있다면 제외해주기
    h = []
    for i in d:
        g = []
        g.append(''.join(i))
        result = ''.join(g)
        result = result.replace('1.0', '')
        h.append(result)
    '''
    print(h)
    ['2a2ba3c', 'aabbaccc', 'aabbaccc', 'aabbaccc', 'aabbaccc', 'aabbaccc', 'aabbaccc', 'aabbaccc']
    '''

    # 길이 구하기
    q = []
    for i in range(len(h)):
        q.append(len(h[i]))
    '''
    print(q)
    [7, 8, 8, 8, 8, 8, 8, 8]
    '''

    # 최솟값 return
    return min(q)