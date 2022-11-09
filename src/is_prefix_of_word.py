def is_prefix_of_word(sentence, search_word):
    if search_word in sentence:
        words_list = sentence.split(" ")
        for i, word in enumerate(words_list):
            index = word.find(search_word)
            if index == 0:
                return i
    return -1
