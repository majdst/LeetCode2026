class Node:

    def __init__(self, data:int, next=None):

        self.data = data
        self.next = next

class LinkedList:
    def helperfun(self, l:list):
        
        dummy = Node(0)
        current = dummy

        for num in l:
            current.next = Node(num)
            current = current.next
        
        return dummy.next
    
    def print(self, l):

        while l is not None:
            print(l.data, end = " -> ")
            l = l.next

        print("None")

    def MergeTwoListSorted(self, l1:list, l2:list)->list:

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        dummy = Node(0)
        current = dummy

        while l1 is not None and l2 is not None:

            if l1.data < l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if l1 is not None:
            current.next = l1
        else:
            current.next = l2
        
        return dummy.next


mylist = LinkedList()

x1 = mylist.helperfun([1,2,4])
x2 = mylist.helperfun([1,3,4])
mylist.print(x1)
mylist.print(x2)
print("*****************")

x3 = mylist.MergeTwoListSorted(x1, x2)
mylist.print(x3)


    
    #Inefficient way of solving this question
    # def helper(self, l:list):

    #     dummy = Node(0)

    #     current = dummy

        
    #     for num in l:

    #             current.next = Node(num)
    #             current = current.next

    #     return dummy.next
    
    # def printout(self, node:list):

    #     while node is not None:

    #         print(node.data, end=" -> ")

    #         node = node.next
    #     print("None")

    # def sort(self, l1:list):
        
    #     if l1 is None:
    #         return
        
    #     swapped = True
    #     while swapped:

    #         swapped = False
    #         current = l1

    #         while current.next is not None:

    #             if current.data > current.next.data:
    #                 current.data, current.next.data = current.next.data, current.data

    #                 swapped = True
                
    #             current = current.next
    #     return l1

    # def merge(self, l1:list, l2:list)->list:
        
    #     if l1 is None:
    #         return l2
    #     if l2 is None:
    #         return l1
        
    #     current = l1
    #     while current.next is not None:

    #         current = current.next

    #     current.next = l2

    #     self.sort(l1)

    #     return l1




# mylist = LinkedList()

# x1 = mylist.helper([1,2,4])
# x2 = mylist.helper([1,3,4])

# mylist.printout(x1)
# mylist.printout(x2)
# print("***********")
# x3 = mylist.merge(x1, x2)
# mylist.printout(x3)
# print("**************")


