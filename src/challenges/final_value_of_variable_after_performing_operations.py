def final_value_after_operations(operations):
    plus = '+'
    x = 0
    for op in operations:
        if plus in op:
            x += 1
        else:
            x -= 1
    return x
