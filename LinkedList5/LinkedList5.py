class Node:
    def __init__(self, data:int, next = None):

        self.data = data
        self.next = next

class LinkedList:
    def helperFunction(self, l:Node):

        dummy = Node(0)
        current = dummy

        for i in l:
            current.next = Node(i)
            current = current.next

        return dummy.next
    
    def print(self, l:Node):

        while l is not None:
            print(l.data, end = " -> ")

            l = l.next
        print("None")

    
    def lenLink(self, l:Node):
        len = 0

        while l is not None:
            l = l.next

            len+=1
        return len
    
    def middlelist(self, l:Node):
        
        m = self.lenLink(l)

        if m % 2 != 0:
            middle = m // 2

        else:
            middle = m // 2

        current = l
        for i in range(middle):

            current = current.next
        
        return current.data







mylist = LinkedList()

x1 = mylist.helperFunction([1])
mylist.print(x1)
print(mylist.lenLink(x1))
print("***********")

print(mylist.middlelist(x1))
