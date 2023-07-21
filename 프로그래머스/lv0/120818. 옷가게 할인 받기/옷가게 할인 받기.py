def solution(price):
    result = 0
    if 100000 <= price < 300000:
        result = price * 0.95
        return int(result)
    elif 300000 <= price < 500000:
        result = price * 0.9
        return int(result)
    elif 500000 <= price <= 1000000:
        result = price * 0.8
        return int(result)
    else:
        return price