def duplicate_count(text):
    cnt = 0
    text = text.lower()
    tex = set(text)
    for i in tex:
        if text.count(i) >= 2:
            cnt += 1
    return cnt
