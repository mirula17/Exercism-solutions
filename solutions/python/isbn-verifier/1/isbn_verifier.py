def is_valid(isbn):
    isbn = isbn.replace("-", "")
    
    if len(isbn) != 10:
        return False
    
    total = 0
    
    for i in range(10):
        char = isbn[i]
        
        if char == "X":
            if i != 9:
                return False
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False
        
        total += value * (10 - i)
    
    return total % 11 == 0
