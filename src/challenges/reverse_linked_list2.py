# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # Get the node with value == left
        current_node = head
        prev = None
        while current_node and current_node.value != left:
            prev = current_node
            current_node = current_node.next
        
        # Get the node with value == right
        prev2 = None
        while current_node and current_node.value != right:
            prev2 = current_node
            current_node = current_node.next
        current_node2 = prev2.next
        next_node2 = current_node.next

        
        
