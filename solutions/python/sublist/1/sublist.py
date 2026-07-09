SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def is_sublist(sub, main):
    if len(sub) == 0:
        return True

    for i in range(len(main) - len(sub) + 1):
        if main[i:i + len(sub)] == sub:
            return True
    return False


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    elif is_sublist(list_one, list_two):
        return SUBLIST
    else:
        return UNEQUAL
        
