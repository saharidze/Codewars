import string


def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return set(c for c in s.lower() if c.isalpha()) == alphabet
