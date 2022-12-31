def count_asterisks(s):
    """
    Time O(N)
    Space O(N)
    """
    pipes_count = 0
    total_askterisk_count = 0
    for c in s:
        if c == '|':
            pipes_count += 1
        if (pipes_count % 2 == 0 or pipes_count == 0) and c == '*':
            total_askterisk_count += 1
    return total_askterisk_count
