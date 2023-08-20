def solution(my_string, index_list):
    result = ''
    my_string = list(my_string)
    for i in range(len(index_list)):
        result += ''.join(my_string[index_list[i]])
    return result