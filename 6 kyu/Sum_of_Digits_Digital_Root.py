def digital_root(n):
    while n > 9:
        n = n // 10 + n % 10
    return n
