# O(n) Time
# O(n) Space where n is the length of string
def is_palindrome(string: str) -> bool:

    cleaned_string = ""
    for c in string:
        if c.isalnum():
            cleaned_string += c

    return cleaned_string == cleaned_string[::-1]


# Even better solution for optimized memory

# O(n) Time
# O(1) Space


def is_palindrome_optimized_memory(string):

    # Two pointers beginning and end
    i = 0
    j = len(string) - 1

    while i < j:

        # Skip non alphanumeric characters

        while not string[i].isalnum() and i < j:
            i += 1

        while not string[j].isalnum() and i < j:
            j -= 1

        if string[i].lower() != string[j].lower():
            return False

        i += 1
        j -= 1

    return True
