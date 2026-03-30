def rotate(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = (ord(char) - ord('a') + key) % 26
                result += chr(shifted + ord('a'))
            else:
                shifted = (ord(char) - ord('A') + key) % 26
                result += chr(shifted + ord('A'))
        else:
            result += char

    return result