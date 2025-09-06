import secrets
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    charset = string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation

    if not charset:
        raise ValueError("Zaznacz przynajmniej jeden typ znaków.")

    return ''.join(secrets.choice(charset) for _ in range(length))
