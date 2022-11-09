def is_prefix_of_word(sentence, search_word):
    if search_word in sentence:
        words_list = sentence.split(" ")
        for i, word in enumerate(words_list):
            index = word.find(search_word)
            if index == 0:
                return i + 1
    return -1


print(is_prefix_of_word(sentence="i love eating burger", search_word="burg"))
print(is_prefix_of_word(sentence="this problem is an easy problem", search_word="pro"))
print(is_prefix_of_word(sentence="i am tired", search_word="you"))
