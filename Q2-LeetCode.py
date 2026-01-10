class Node:
    def __init__(self, data:int, next=None):

        self.data = data
        self.next = next

class LinkedList:

    def addTwoNumber(self, l1:Node, l2:Node)->Node:

        dumy = Node(0)
        current = dumy
        remain = 0

        while l1 is not None or l2 is not None or remain != 0:


            val1 = l1.data if l1 is not None else 0
            val2 = l2.data if l2 is not None else 0

            total = val1 + val2 + remain

            remain = total // 10
            rem = total % 10

            current.next = Node(rem)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            
        return dumy.next
    
    #Helper function to create a list
    def list_model(self, l:list):

        dummy = Node(0)
        current = dummy

        for number in l:
            current.next = Node(number)

            current = current.next

        return dummy.next
    
    def print_func(self, node):

        while node is not None:

            print(node.data, end=" -> ")

            node = node.next

        print("None")


mylist = LinkedList()
x1 = mylist.list_model([9,9,9,9,9,9,9])
x2 = mylist.list_model([9,9,9,9])

print("*************")
mylist.print_func(x1)
mylist.print_func(x2)
print("**************")

y = mylist.addTwoNumber(x1, x2)
print("****************")
mylist.print_func(y)





