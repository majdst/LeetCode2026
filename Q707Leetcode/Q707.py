class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index:int) -> int:

        if index < 0 or index >= self.size:
            return -1
        
        current = self.head

        for i in range(index):
            current = current.next
        return current.val
    
    def addAtHead(self, val: int) -> None:

        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    
    def addAtTail(self, val:int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode

        current = self.head
        while current.next:
            current = current.next
        
        current.next = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            return self.addAtTail(Node(val))
        
        newNode = Node(val)
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        current.next = newNode
        newNode.next = current.next

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:
            return 
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        
        current = self.head
        for i in range(index - 1):
            current = current.next

        current.next = current.next.next
        self.size -= 1

