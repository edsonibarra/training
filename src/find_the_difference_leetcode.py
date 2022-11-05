def find_the_diffrence(s, t):

    letters = {}
    for c in s:
        letters[c] = letters.get(c,0) + 1

    letters_plus_one = {}
    for c in t:
        letters_plus_one[c] = letters_plus_one.get(c,0) + 1

    for c in letters_plus_one:
        if c not in letters or letters[c] != letters_plus_one[c]:
            return c
