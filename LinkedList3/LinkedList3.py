class Node:
    def __init__(self, data:int):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data:int):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def preprint(self):

        current = self.head

        while current is not None:
            print(current.data, end= " -> ")

            current = current.next
        
        print("None")

    def reverse(self):

        current = self.head
        back = None

        while current is not None:
            
            next_node = current.next
            current.next = back #reverse 

            back = current
            current = next_node
        
        self.head = back

mylist = LinkedList()
mylist.append(5)
mylist.append(10)
mylist.append(15)
mylist.preprint()
mylist.reverse()
mylist.preprint()