def is_palindrome(string: str) -> bool:

    cleaned_string = ""
    for c in string:
        if c.isalnum():
            cleaned_string += c

    return cleaned_string == cleaned_string[::-1]