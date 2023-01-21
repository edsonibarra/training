class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, idx):
        if self.is_empty():
            return -1
        current_node = self.head
        count = 0
        while current_node and count != idx:
            count += 1
            current_node = current_node.next
        if current_node:
            return current_node.val
        else:
            return  -1
    
    def addAtHead(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            return
        current_node = self.head
        new_node.next = current_node
        self.head = new_node
    
    def addAtTail(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            currnet_node = current_node.next
        current_node.next = new_node
    
    def addAtIndex(self, idx, val):
        count = 0
        new_node = Node(val)
        cur_node = self.head
        prev = None 
        while cur_node and count != idx:
            prev = cur_node
            count += 1
            cur_node=  cur_node.next
        if cur_node:
            prev.next = new_node
            new_node.next = cur_node
    def deleteAtIndex(self, val):
        if self.is_empty():
            return -1
        
        
        current_node = self.head
        count = 0
        prev = None
        if prev == count:
            self.head = current_node.next
            current_node = None
            return
        while current_node and count != val:
            prev = current_node
            current_node = current_node.next
        if current_node:
            prev.next = current_node.next
            current_node = None
            return
        else:
            return -1
            
    
    def is_empty(self):
        return self.head is None
