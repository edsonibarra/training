def is_circular_linked_list(input_list):
    """
    Checkes if the input_list parameter is a circular linked list or not
    If it's a linked list returns True otherwise returns False
    """

    head_ = input_list.head
    cur_node = input_list.head
    while cur_node.next:
        if cur_node.next == head_:
            return True
        cur_node = cur_node.next
    return False

