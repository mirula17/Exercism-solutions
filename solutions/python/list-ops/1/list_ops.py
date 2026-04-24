def append(list1, list2):
    result = []
    for item in list1:
        result = result + [item]
    for item in list2:
        result = result + [item]
    return result


def concat(lists):
    result = []
    for lst in lists:
        for item in lst:
            result = result + [item]
    return result


def filter(function, lst):
    result = []
    for item in lst:
        if function(item):
            result = result + [item]
    return result


def length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def map(function, lst):
    result = []
    for item in lst:
        result = result + [function(item)]
    return result


def foldl(function, lst, initial):
    result = initial
    for item in lst:
        result = function(result, item)
    return result


def foldr(function, lst, initial):
    result = initial
    index = length(lst) - 1
    
    while index >= 0:
        result = function(result, lst[index])
        index -= 1
    
    return result


def reverse(lst):
    result = []
    for item in lst:
        result = [item] + result
    return result