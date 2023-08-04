def make_readable(s):
    h = s // 3600
    m = (s - 3600 * h) // 60
    s = s - 3600 * h - m * 60
    return f"{h:02d}:{m:02d}:{s:02d}"
