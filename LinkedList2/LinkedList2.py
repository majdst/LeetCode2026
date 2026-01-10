class Node:
    def __init__(self, data:int):

        self.data = data
        self.next = None

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

    def remove_duplicate(self):

        current = self.head
        #Important--> and --> In barai inke ke agar akhari tail bod-->Error nade
        while current is not None and current.next is not None:
            
            if current.data == current.next.data:
                current.next = current.next.next
            
            else:
                current = current.next


    def pre_print(self):

        if self.head is None:
            return
        
        current = self.head
        while current is not None:

            print(f"{current.data}", end = " -> ")

            current = current.next
        print("None")


mylist = LinkedList()
mylist.append(1)
mylist.append(1)
mylist.append(1)
# mylist.append(2)
# mylist.append(2)
# mylist.append(3)
# mylist.append(3)
# mylist.append(3)
# mylist.append(4)
mylist.pre_print()
mylist.remove_duplicate()
mylist.pre_print()