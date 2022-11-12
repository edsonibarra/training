def find_occurrences(text, first, second):
    text_list = text.split(" ")
    i = 0
    ans = []
    while i < len(text_list) - 2:
        if text_list[i] == first and text_list[i + 1] == second:
            ans.append(text_list[i + 2])
        i += 1
    return ans


print(
    find_occurrences(
        text="alice is a good girl she is a good student", first="a", second="good"
    )
)
