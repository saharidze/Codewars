from __future__ import annotations


def dig_pow(n, p):
    digits = [int(d) for d in str(n)]
    digit_powers = [d ** (p + i) for i, d in enumerate(digits)]
    if sum(digit_powers) % n == 0:
        return sum(digit_powers) // n
    else:
        return -1
