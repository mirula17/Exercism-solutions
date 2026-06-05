def sum_of_multiples(level, factors):
    multiples = set()

    for factor in factors:
        if factor == 0:
            continue

        for num in range(factor, level, factor):
            multiples.add(num)

    return sum(multiples)
