from __future__ import annotations


def array_diff(a, b):
    return [x for x in a if x not in b]
