def grabscrab(said, possible_words):
    word_sorted = sorted(said)
    return [word for word in possible_words if sorted(word) == word_sorted]
