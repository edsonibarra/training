# O(n) Time
# O(1) space


def detect_capital(word):
    if word.isupper():
        return True
    elif word.islower():
        return True
    elif word and word[0].isupper():
        return word[1:].islower()
    return False
    