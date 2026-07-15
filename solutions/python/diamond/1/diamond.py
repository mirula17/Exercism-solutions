def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = alphabet.index(letter)
    size = 2 * n + 1
    diamond = []

    # Top half (including middle)
    for i in range(n + 1):
        ch = alphabet[i]
        outer_spaces = n - i

        if i == 0:
            row = " " * outer_spaces + ch + " " * outer_spaces
        else:
            inner_spaces = 2 * i - 1
            row = (
                " " * outer_spaces
                + ch
                + " " * inner_spaces
                + ch
                + " " * outer_spaces
            )

        diamond.append(row)

    # Bottom half
    for i in range(n - 1, -1, -1):
        ch = alphabet[i]
        outer_spaces = n - i

        if i == 0:
            row = " " * outer_spaces + ch + " " * outer_spaces
        else:
            inner_spaces = 2 * i - 1
            row = (
                " " * outer_spaces
                + ch
                + " " * inner_spaces
                + ch
                + " " * outer_spaces
            )

        diamond.append(row)

    return diamond


# Example
for line in rows("E"):
    print(line)
