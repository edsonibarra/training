def most_words_found(sentences):
    current_max = 0
    for sentence in sentences:
        len_sentence = len(sentence.split(' '))
        current_max = max(current_max, len_sentence)
    return current_max
