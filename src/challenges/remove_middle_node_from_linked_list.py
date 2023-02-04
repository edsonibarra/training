class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total_len = self.get_len(head)
        middle = total_len // 2
        if total_len == 1:
            head = None
            return head
        count = 0
        current_node = head
        prev = None
        while current_node and count != middle:
            count += 1
            prev = current_node
            current_node = current_node.next
        
        if current_node:
            prev.next = current_node.next
            current_node = None
            return head

    def get_len(self, head):
        current_node = head
        count = 0
        if head is None:
            return count
        while current_node:
            count += 1
            current_node = current_node.next
        return count