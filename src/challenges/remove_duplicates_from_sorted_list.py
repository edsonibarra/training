# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        prev = None
        while current_node:
            if prev and current_node.val == prev.val:
                prev.next = current_node.next
            else:
                prev = current_node
            current_node = current_node.next
            
        return head
