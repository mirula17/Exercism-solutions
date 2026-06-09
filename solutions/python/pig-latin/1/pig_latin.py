def translate(text):
    words = text.split()
    result = []

    for word in words:
        # Rule 1
        if word.startswith(("a", "e", "i", "o", "u", "xr", "yt")):
            result.append(word + "ay")
            continue

        # Rule 3: consonants + qu
        if "qu" in word:
            idx = word.find("qu")
            if idx == 0 or all(c not in "aeiou" for c in word[:idx]):
                result.append(word[idx + 2:] + word[:idx + 2] + "ay")
                continue

        # Rules 2 and 4
        for i, ch in enumerate(word):
            if ch in "aeiou" or (ch == "y" and i != 0):
                result.append(word[i:] + word[:i] + "ay")
                break

    return " ".join(result)
