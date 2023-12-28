from __future__ import annotations


def rgb(r, g, b):
    r = min(max(r, 0), 255)
    g = min(max(g, 0), 255)
    b = min(max(b, 0), 255)
    return f'{r:02X}{g:02X}{b:02X}'
