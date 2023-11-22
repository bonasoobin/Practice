def solution(my_string):
    string_list = list(my_string)
    unique_set = set(string_list)
    unique_list = sorted(unique_set, key=string_list.index)
    result_string = ''.join(unique_list)
    return result_string