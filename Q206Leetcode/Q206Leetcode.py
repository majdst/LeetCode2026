class Node:
    def __init__(self, val:int, next=None):
        self.val = val
        self.next = next

class Linkedlist:
    def helper(self, l:list):

        dummy = Node(0)
        current = dummy

        for num in l:
            current.next = Node(num)

            current = current.next
        
        return dummy.next
    
    def pr(self, l:Node):

        current = l

        while current:
            print(current.val, end = " -> ")

            current = current.next
        
        print("None")
    
    def reverse(self, l:Node):

        back = None
        current = l
        while current:

            newnode = current.next
            current.next = back #reverse to the last point

            back = current
            current = newnode

        return back
    
x = Linkedlist()
x1 = x.helper([1,2,3,4,5])
x.pr(x1)

x2 = x.reverse(x1)
x.pr(x2)