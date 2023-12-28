from __future__ import annotations


def unique_in_order(s):
    if len(s) == 0:
        return []
    res = list()
    res.append(s[0])
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            res.append(s[i])
    return res
