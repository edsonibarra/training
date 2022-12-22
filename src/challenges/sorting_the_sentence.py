def sorting_the_sentence(s):
    new_sentence = []
    sentence_list = s.split(' ')
    print(f'sentence_list = {sentence_list}')
    
    current_num = 1
    total_len = len(sentence_list)
    
    i = 0
    while sentence_list:
        curr_word = sentence_list[i]
        if int(curr_word[-1]) == current_num:
            new_sentence.append(curr_word[:-1])
            current_num += 1
            i = 0
        else:
            i += 1
        
        if current_num -1 == total_len:
            break
    return ' '.join(new_sentence)
