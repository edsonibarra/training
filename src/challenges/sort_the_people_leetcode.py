def sort_the_people(names, heights):

    heights_names = zip(heights, names)
    heights_first = []

    for height_name in heights_names:
        heights_first.append(height_name)

    answer_sorted = sorted(heights_first)

    answer = []
    for name in answer_sorted[::-1]:
        answer.append(name[1])
    return answer
