# O(n) Time
# O(1) Space


def first_non_repeating_char(string):

    chars = {}
    for c in string:
        chars[c] = chars.get(c, 0) + 1

    for index, c in enumerate(string):
        if chars[c] == 1:
            return index

    return -1
