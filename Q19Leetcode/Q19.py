class Node:
    def __init__(self, val:int, next=None):

        self.val = val
        self.next = next

class LinkedList:

    def helper(self, l:list):

        dummy = Node(0)
        current = dummy

        for num in l:

            current.next = Node(num)
            current = current.next

        return dummy.next
    
    def print(self, l:Node):

        current = l
        while current:

            print(current.val, end = " -> ")

            current = current.next
        print("None")

    def leng(self, l:Node):
        ln = 0
        current = l
        while current:
            current = current.next
            ln += 1
        return ln
    
    def rmvNth(self, head:Node, n:int)->Node:

        
        dummy = Node(0)
        dummy.next = head

        l = dummy #left pointer
        r = dummy #right pointer

        for _ in range(n+1):
            r = r.next #making gap between two pointer

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next



lst = LinkedList()
c1 = lst.helper([1, 2, 3, 5, 6])
c3 = lst.leng(c1)

print(c3)

c2 = lst.rmvNth(c1, 1)
lst.print(c2)
