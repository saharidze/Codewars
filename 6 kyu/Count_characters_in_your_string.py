from __future__ import annotations


def count(s):
    return {i: s.count(i) for i in s}
