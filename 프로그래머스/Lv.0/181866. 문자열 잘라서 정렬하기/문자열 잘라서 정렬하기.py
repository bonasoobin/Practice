def solution(myString):
    answer = []
    myString = myString.split('x')
    for i in range(len(myString)):
        if myString[i] != "":
            answer.append(myString[i])
    return sorted(answer)