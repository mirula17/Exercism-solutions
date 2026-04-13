def find_anagrams(word, candidates):
    result = []
    word_lower = word.lower()
    sorted_word = sorted(word_lower)

    for candidate in candidates:
        candidate_lower = candidate.lower()

        # Skip if it's the same word (case-insensitive)
        if candidate_lower == word_lower:
            continue

        # Check if sorted letters match
        if sorted(candidate_lower) == sorted_word:
            result.append(candidate)

    return result
