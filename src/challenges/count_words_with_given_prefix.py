def count_words(words, pref):
    l = len(pref)
    count = 0
    for word in words:
        print(word[0:l])
        if word[0:l] == pref:
            count += 1
    return count