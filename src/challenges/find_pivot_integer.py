def pivot_integer(n):
    if n == 1:
        return n
    n_list = [n for n in range(1, n + 1)]
    last_index = len(n_list) - 1 - 1
    while last_index >= 1:
        left = n_list[:last_index + 1]
        right = n_list[last_index:]
        if sum(left) == sum(right):
            return n_list[last_index]
        last_index -= 1
