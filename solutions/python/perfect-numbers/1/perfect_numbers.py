def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = 1 if number > 1 else 0

    i = 2
    while i * i <= number:
        if number % i == 0:
            aliquot_sum += i
            if i != number // i:
                aliquot_sum += number // i
        i += 1

    if number == 1:
        aliquot_sum = 0

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
