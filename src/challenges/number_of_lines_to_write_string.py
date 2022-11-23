def number_of_lines_to_write_string(widths, s):
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    mapping = {}
    for i in range(len(all_letters)):
        mapping[all_letters[i]] = i
    print(mapping)

    count = 100
    total_lines = 0

    for c in s:
        if count < widths[mapping[c]]:
            total_lines += 1
            count = 100
        print(c)
        count -= widths[mapping[c]]
    if count != 0 or count == 0:
        total_lines += 1

    return [total_lines, 100 - count]