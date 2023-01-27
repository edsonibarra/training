# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current_node = head
        items = []
        while current_node:
            items.append(current_node.val)
            current_node = current_node.next

        return items == items[::-1]
