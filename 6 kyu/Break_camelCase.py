from __future__ import annotations


def solution(s):
    res = ''
    for i in s:
        if i.upper() == i:
            res += ' ' + i
        else:
            res += i
    return res
