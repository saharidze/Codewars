from __future__ import annotations


def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
