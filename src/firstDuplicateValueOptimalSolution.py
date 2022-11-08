def firstDuplicateValueOptimalSolution(array):
    """Optimal Solution"""
    for value in array:
        absolute_value = abs(value)
        if array[absolute_value - 1] < 0:
            return absolute_value
        array[absolute_value - 1] *= -1
    return -1
