class Node:
    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head

            while current.next is not None:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

mylist = LinkedList()
mylist.append(100)
mylist.append(3)
mylist.append(0)
mylist.append(20)
mylist.append(102)
mylist.append(39)

mylist.print()
print("***********")

mylist.sort()
mylist.print()
