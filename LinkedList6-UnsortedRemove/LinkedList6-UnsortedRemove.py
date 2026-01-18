class Node:

    def __init__(self, data:int, next=None):

        self.next = next
        self.data = data

class LinkedList:

    def helperfunc(self, l:list):

        dummy = Node(0)
        curr = dummy

        for num in l:

            curr.next = Node(num)

            curr = curr.next
        
        return dummy.next
    
    def print(self, l:Node):

        while l is not None:
            print(l.data, end = " -> ")

            l = l.next

        print("None")

    def removeUnsort(self, l:Node):
        
        seen = set()
        current = l
        back = None

        while current is not None:

            if current.data in seen:

                back.next = current.next #skip the current

            else:
                seen.add(current.data)
                back = current
            
            current = current.next

        return l


mylist = LinkedList()
x1 = mylist.helperfunc([1,2, 2, 3, 4, 4, 5, 6, 7, 7, 7, 7, 2, 5, 4,8,9])
mylist.print(x1)
print("*************")
x2 =mylist.removeUnsort(x1)
mylist.print(x2)
