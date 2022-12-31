def halves_are_alike(s):
    vowels = "aeiou"
    m = len(s) // 2
    left = s[:m]
    right = s[m:]
    i = 0
    vowels_in_left = 0
    vowels_in_right = 0
    while i < len(left):
        if left[i].lower() in vowels:
            vowels_in_left += 1
        
        if right[i].lower() in vowels:
            vowels_in_right += 1
        
        i += 1
    return vowels_in_left == vowels_in_right



