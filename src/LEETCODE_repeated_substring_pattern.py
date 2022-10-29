# This is not from ALGOEXPERT.IO
# This is a challenge from Leetcode.com 

def repeated_substring_pattern(s):
    s1 = s+s
    s2 = s1[1:-1]
    return s in s2
