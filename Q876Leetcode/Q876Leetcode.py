class Node:

    def __init__(self, val:int, next = None):

        self.next = next
        self.val = val

class LinkedList:
    def helper(self, l:list)->Node:

        dummy = Node(0)
        current = dummy

        for i in l:
            newnode = Node(i)

            current.next = newnode
            current = current.next

        return dummy.next
    
    def pr(self, l:Node):

        current = l

        while current:
            print(current.val, end = " -> ")
            current = current.next
        print("None")

    def middle(self, l:Node):
        right, left = l, l
        while right and right.next:
            left = left.next
            right = right.next.next

        return left    
x = LinkedList()
x1 = x.helper([1,2,3,4,5])
x.pr(x1)
x.pr(x.middle(x1))
