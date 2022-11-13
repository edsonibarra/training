def most_common(paragraph, banned):
    i = 0
    new_word = ''
    words = []
    while i < len(paragraph):
        current = paragraph[i]
        if current.isalnum():
            new_word += current
        else:
            if new_word:
                words.append(new_word.lower())
            new_word = ''
        i+= 1
    if new_word:
        words.append(new_word.lower())
    print(words)
    d = {}
    for word in words:
        d[word] = d.get(word,0)+1
    
    print(d)
    max_values = ("",0)
    for word,value in d.items():
        if value > max_values[1] and word not in banned:
            max_values = (word,value)
    return max_values[0]
print(most_common("a, a, a, a, b,b,b,c, c",["a"]))
print(most_common(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(most_common(paragraph = "a.", banned = []))
print(most_common(paragraph="Bob", banned=[]))