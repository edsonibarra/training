def count_items_matching_a_rule(items, ruleKey, ruleValue):
    keys_indexes = [(0,'type'), (1, 'color'), (2, 'name')]

    lookup_index = 0
    for index, key in keys_indexes:
        if key == ruleKey:
            lookup_index = index
    
    total_count = 0
    for item in items:
        if item[lookup_index] == ruleValue:
            total_count += 1
    return total_count
