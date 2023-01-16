def is_circular_sentence(sentence):
    first_letter = sentence[0]
    idx = 0
    before_space = ""
    after_space = ""
    while idx < len(sentence):
        if not sentence[idx].isalpha():
            before_space = sentence[idx - 1]
            after_space = sentence[idx + 1]
        if before_space != after_space:
            return False
        last_letter = sentence[idx]
        idx += 1
    return first_letter == last_letter
