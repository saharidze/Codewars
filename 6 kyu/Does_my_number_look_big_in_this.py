def narcissistic(value):
    res = 0
    n = len(str(value))
    for i in str(value):
        res += int(i) ** n
    return res == value
