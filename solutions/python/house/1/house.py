VERSES = [
    ("the house that Jack built.", ""),
    ("the malt", "that lay in"),
    ("the rat", "that ate"),
    ("the cat", "that killed"),
    ("the dog", "that worried"),
    ("the cow with the crumpled horn", "that tossed"),
    ("the maiden all forlorn", "that milked"),
    ("the man all tattered and torn", "that kissed"),
    ("the priest all shaven and shorn", "that married"),
    ("the rooster that crowed in the morn", "that woke"),
    ("the farmer sowing his corn", "that kept"),
    ("the horse and the hound and the horn", "that belonged to"),
]


def recite(start_verse, end_verse):
    result = []

    for i in range(start_verse - 1, end_verse):
        parts = ["This is " + VERSES[i][0]]

        for j in range(i, 0, -1):
            action = VERSES[j][1]
            subject = VERSES[j - 1][0]
            parts.append(f"{action} {subject}")

        result.append(" ".join(parts))

    return result
