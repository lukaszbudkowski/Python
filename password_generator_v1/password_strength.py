import string

def evaluate_strength(password):
    length = len(password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 12 and score == 4:
        return "Silne"
    elif length >= 8 and score >= 3:
        return "Średnie"
    else:
        return "Słabe"
