class Node:

    def __init__(self, data:int, next=None):
        self.data = data
        self.next = next

class NodeLinked:

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


    def prepend(self, data:int):

        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node


    def preprint(self):
        current = self.head

        while current is not None:
            print(current.data, end = " -> ")

            current = current.next

        print("None")
    
    def search(self, data:int):

        if self.head is None:
            return
        
        current = self.head
        position = 0
        while current.next is not None:

            if current.data == data:

                print(f"{current.data} is in {position}")
            position += 1
            current = current.next

    def get_length(self):

        current = self.head
        len = 0

        while current is not None:
            len += 1

            current = current.next
        print(f"length of linkedlist is {len}")





mylist = NodeLinked()

mylist.append(10)
mylist.append(100)
mylist.append(2)
mylist.append(50)
mylist.prepend(39)

mylist.preprint()

mylist.search(2)

mylist.get_length()