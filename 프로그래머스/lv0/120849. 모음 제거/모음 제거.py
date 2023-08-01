def solution(my_string):
    col = ("a,e,i,o,u")
    for i in col:
        my_string = my_string.replace(i,"")
    return my_string