class Node:

    def __init__(self, data:int, next = None):

        self.data = data
        self.next = next

class LinkedList:

    def helper(self, l:Node):

        dummy = Node(0)
        current = dummy

        for num in l:

            current.next = Node(num)
            current = current.next

        return dummy.next
    
    def print(self, l:Node):

        current = l

        while current is not None:

            print(current.data, end = " -> ")
            current = current.next

        print("None")

    def search(self, l:Node, item:int):


        current = l
        position = 0

        while current is not None:

            if current.data == item:
                print(f"{current.data} is in {position}")
            
            


            position += 1

            current = current.next

    def get_length(self, l:Node):

        current = l
        count = 0
        while current:

            count += 1
            current = current.next

        return count
     
    def sortlinkRemove(self, l:Node):

        current = l

       

        while current and current.next:

                if current.data == current.next.data:
                    current.next = current.next.next

                    
                else:
                    current = current.next
        return l

    def unsortedLinkRemove(self, l:Node):
        return 
    
    def reverse(self, l:Node):

        current = l

        back = None

        while current:

            next_node = current.next

            current.next = back

            back = current
            current = next_node

        l = back
        return l
    
    def sortlist(self, l:Node):

        

        sw = True

        while sw:

            sw = False
            current = l

            while current and current.next:

                if current.data > current.next.data:

                    current.data, current.next.data = current.next.data, current.data
                    sw = True
                
                current = current.next

        return l


mylist = LinkedList()
x1 = mylist.helper([1,1,1,2,2,8,4,5,6,14, 6,6,7,7,7,7,7,8])
mylist.print(x1)
print("************")

# x2 = mylist.search(x1, 2)

# print("***************")

# x3 = mylist.get_length(x1)
# print(x3)

# print("***************")
# x4 = mylist.sortlinkRemove(x1)
# mylist.print(x4)

# print("****************")
# x5 = mylist.reverse(x1)
# mylist.print(x5)

print("****************")
x6 = mylist.sortlist(x1)
mylist.print(x6)

