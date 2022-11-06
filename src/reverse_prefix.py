def reverse_prefix(word, ch):
    if ch in word:
        index = word.find(ch)
        return word[:index+1][::-1]+word[index+1:]
    return word