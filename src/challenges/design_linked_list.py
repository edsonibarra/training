class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        count = 0
        if index == count:
            return self.head
        cur = self.head
        while cur and count != index:
            count += 1
            cur = cur.next
        
        if cur:
            return cur.val
        
    def addAtHead(self, val: int) -> None:
        
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        new_node.next = cur
        self.head = new_node
        self.len += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len - 1:
            return
        

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        prev = None
        cur = self.head
        count = 0
        if index == count:
            self.head = cur.next
            cur = None
            return
        
        while cur and count != index:
            prev = cur
            cur = cur.nex

        if cur:
            prev.next = cur.next
            cur = None
            return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

