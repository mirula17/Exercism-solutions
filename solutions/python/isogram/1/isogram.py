def is_isogram(word):
    seen = set()

    for char in word.lower():
        if char.isalpha():  # ignores spaces, hyphens, symbols
            if char in seen:
                return False
            seen.add(char)

    return True