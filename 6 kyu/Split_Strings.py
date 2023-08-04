def solution(s):
    return [
        s[i : i + 2] if len(s[i : i + 2]) == 2 else s[i] + "_"
        for i in range(0, len(s), 2)
    ]
