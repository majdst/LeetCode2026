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

        position = 0
        current = head
        

        m = self.leng(head)
        p = m - n

        if p == 0:
            return current.next
        
        while current:

            if position == p -1:
                current.next = current.next.next

            current = current.next
            position +=1
        
        return head
        
lst = LinkedList()
c1 = lst.helper([1])
c3 = lst.leng(c1)

print(c3)

c2 = lst.rmvNth(c1, 1)
lst.print(c2)
