def to_goat_latin(sentence):

    vowels = 'aeiouAEIOU'
    begins_vow = 'ma'
    words_list = sentence.split(' ')
    
    ans = []

    i = 0
    while i < len(words_list):

        curr_word = words_list[i]
        
        if curr_word[0] not in vowels:
            
            new_word = curr_word[1:] + curr_word[0] + "ma"

        else:
            
            new_word = curr_word + begins_vow

        new_word += (i + 1) * 'a'
        ans.append(new_word)

        i += 1

    return " ".join(ans)