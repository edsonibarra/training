def LC_28(haystack, needle):
    """
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    """
    if needle in haystack:
        needle_len = len(needle)
        i = 0
        while i < len(haystack):
            substring = haystack[i:i+needle_len]
            if substring == needle:
                return i
    return -1