import string

# Create mapping dictionaries
plain = string.ascii_lowercase
cipher = plain[::-1]

encode_map = str.maketrans(plain, cipher)
decode_map = str.maketrans(cipher, plain)


def encode(text):
    # Remove punctuation, keep letters and digits
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())

    # Translate letters
    encoded = cleaned.translate(encode_map)

    # Group into chunks of 5 characters
    return ' '.join(encoded[i:i+5] for i in range(0, len(encoded), 5))


def decode(text):
    # Remove spaces
    cleaned = text.replace(" ", "")

    # Translate back
    return cleaned.translate(decode_map)


# Example Usage
print(encode("test"))  # gvhg
print(encode("x123 yes"))  # c123b vh
print(decode("gvhg"))  # test
print(decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"))
# thequickbrownfoxjumpsoverthelazydog