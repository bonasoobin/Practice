def solution(quiz):
    result = []
    for i in range(len(quiz)):
        before = quiz[i].split('=')[0].replace(" ", "")
        after = quiz[i].split('=')[1].replace(" ", "")
        if eval(before) == int(after):
            result.append("O")
        else:
            result.append("X")
    return result 