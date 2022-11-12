def count_prefixes(words, s):
    count = 0
    for word in words:
        if word in s:
            index = s.find(word)
            if index == 0:
                count += 1
    return count
