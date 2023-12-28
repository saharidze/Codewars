from __future__ import annotations


def tribonacci(s, n):
    if len(s) >= n:
        return s[:n]
    for i in range(n - len(s)):
        s.append(sum(s[-3:]))
    return s
