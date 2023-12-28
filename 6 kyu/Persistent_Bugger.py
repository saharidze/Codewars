from __future__ import annotations


def persistence(num):
    count = 0
    while len(str(num)) > 1:
        digits = [int(digit) for digit in str(num)]
        num = 1
        for digit in digits:
            num *= digit
        count += 1
    return count
