class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Soultion:
    def helper(self, l:list):
        dummy = ListNode(0)
        current = dummy
        

        for i in l:
            current.next = ListNode(i)
            current = current.next
        
        return dummy.next
    
    def print(self, l):
        current = l

        while current:
            print(current.val, end="->")
            current = current.next
        print("None")
    def oddEvenList(self, head):

        odd = head
        even = head.next
        Heven = even

        while even and even.next:

            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = Heven

        return head
    
x = Soultion()
y = x.helper([2,1,3,5,6,4,7])
x.print(y)
z = x.oddEvenList(y)
x.print(z)