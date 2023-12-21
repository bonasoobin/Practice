def solution(id_pw, db):
    count0 = 0
    count1 = 0
    a = []
    for i in range(len(db)):
        if id_pw[0] == db[i][0]:
            count0 += 1
            a = db[i]

    if count0 >= 1:
        for i in range(len(a)):
            if id_pw[1] == a[1]:
                count1 += 1
    elif count0 == 0:
        return "fail"
    
    if (count1 >=1) & (count1 >= 1):
        return "login"
    elif (count0 >= 1) & (count1 == 0):
        return "wrong pw"