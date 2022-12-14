def valid_subsequence(array, sequence):
    pointerArray = 0
    pointerSquence = 0
    completedSuccess = len(sequence)
    while pointerSquence < len(sequence) and pointerArray < len(array):
        if sequence[pointerSquence] == array[pointerArray]:
            pointerArray += 1
            pointerSquence += 1
        else:
            pointerArray += 1
    print(pointerSquence, completedSuccess)
    if sequence and pointerSquence == completedSuccess:
        return True
    return False
