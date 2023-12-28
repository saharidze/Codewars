from __future__ import annotations


def wave(str):
    result = []
    for i in range(len(str)):
        if str[i].isspace():
            continue
        result.append(str[:i] + str[i].upper() + str[i + 1:])
    return result
