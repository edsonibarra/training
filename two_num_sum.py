def two_number_sum(array, target_sum):
    """
    We are given an array of integers.
    We need to find wich numbers from array sum up to target.
    
    Explanation:
    If we sort the array and use two pointer to each side if the array
    left and right.
    The we check the sum of array[left] + array[right] if equals to target
    return [left, right] otherwise we need to check if the result of the sum
    is grater than target, if it is we substract 1 to right moving this
    point one place to the left and if result if less than target
    we add 1 to left moving the left pointer to right one place untill
    we sum up to the given target.

    Example:
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    array_sorted:
                    [-4, -1, 1, 3, 5, 6, 8, 11]
                    <------------------------->
                    lower values----greater values
    
    result < target:
        move the left pointer to a greater value than the current value
        eg: from -4 to -1
    result > target:
        move the right pointer to a lower value than the current value
        eg: from 11 to 8
    
    """
    pass
    
    
    
