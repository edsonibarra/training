# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head
        total_len = self.get_len(head)
        point = total_len - n
        prev = None 
        count = 0
        if total_len == n:
            head = current_node.next
            current_node = None
            return head
        
        while current_node and count != point :
            count += 1
            prev = current_node
            # print(current_node.val,end='->')
            current_node = current_node.next
        # print('None')
        if current_node:
            prev.next = current_node.next
            current_node = None
            return head
        return head

    
    def get_len(self, head):
        if head is None:
            return 0
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count