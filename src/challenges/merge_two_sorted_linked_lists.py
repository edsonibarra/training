# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        smaller = None
        if list1 and list2:
            if list1.val <= list2.val:
                smaller = list1
                list1 = smaller.next
            else:
                smaller = list2
                list2 = smaller.next
            new_head = smaller

        while list1 and list2:
            if list1.val <= list2.val:
                smaller.next = list1
                smaller = list1
                list1 = smaller.next
            else:
                smaller.next = list2
                smaller = list2
                list2 = smaller.next
        
        if not list1:
            smaller.next = list2
        if not list2:
            smaller.next = list1

        self.head = new_head
        return self.head
