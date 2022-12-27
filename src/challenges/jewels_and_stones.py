def num_jewels_in_stones(jewels, stones):
    
    total_jewels = 0
    for stone in stones:
        if stone in jewels:
            total_jewels += 1

    return total_jewels
