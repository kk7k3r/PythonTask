import re


def password_is_valid(password: str):
    """
    >>> password_is_valid('rtG3FG!Tr^e')
    True
    >>> password_is_valid("aA1!*!1Aa")
    True
    >>> password_is_valid("oF^a1D@y5e6")
    True
    >>> password_is_valid("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >>> password_is_valid("пароль")
    False
    >>> password_is_valid("password")
    False
    >>> password_is_valid("qwerty")
    False
    >>> password_is_valid("lOngPa$$$W0Rd")
    False
    """
    pattern  = re.compile(r'^(?=.*[A-Z].*[A-Z])(?=.*\d)(?=.*[!@#$%^&*?])(?!.*(.)\1\1)[A-Za-z\d!@#$%^&*?]{6,}$')
    return bool(pattern.match(password))

if __name__ == "__main__":
    import doctest
    doctest.testmod()