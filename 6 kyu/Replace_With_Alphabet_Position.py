def alphabet_position(text):
    result = []
    for char in text:
        if char.isalpha():
            char = char.lower()
            position = ord(char) - ord('a') + 1
            result.append(str(position))
    return ' '.join(result)
