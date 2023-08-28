def solution(my_string, is_prefix):
    a = len(is_prefix)
    if my_string[:a] == is_prefix:
        return 1
    else:
        return 0