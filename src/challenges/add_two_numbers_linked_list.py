"""
# 2
"""


def add_two_numbers(l1, l2):
    number_1 = ""
    number_2 = ""

    while l1:
        number_1 += str(l1.val)
        l1 = l1.next

    while l2:
        number_2 += str(l2.val)
        l2 = l2.next

    print(number_1 + "\n" + number_2)

    sum_ = str(int(number_1) + int(number_2))[::-1]

    print(f'Sum='sum_)
    
    self.head = None
    self.head = ListNode(val=int(sum_[0]), next=None)
    cur = self.head
    for c in sum_[1:]:
        while cur.next:
            cur = cur.next
        cur = ListNode(val=int(c))
    return self.head
