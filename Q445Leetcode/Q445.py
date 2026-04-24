class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def helper(self, x:list):
        l = len(x)
        dummy = Node(0)
        current = dummy
        for i in range(l):
            current.next = Node(x[i])
            current = current.next
        return dummy.next
    
    def print(self, x):

        while x:
            print(x.val, "->", end="")
            x = x.next
        print("None")


    def addTwoNumber(self, l1, l2):
        def reverse(x):
            current = x
            back = None
            while current:
                newNode = current.next
                current.next = back

                back = current
                current = newNode
            return back
        l1 = reverse(l1)
        l2 = reverse(l2)
        res = 0
        dummy = Node(0)
        current = dummy
        while l1 or l2 or res != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            trg = val1 + val2 + res

            residual = trg % 10
            res = trg // 10

            newNode = Node(residual)
            current.next = newNode
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return reverse(dummy.next)


x = Solution()
y = x.helper([7,2,4,3])
z = x.helper([5,6,4])
#x.print(y)
x1 = x.addTwoNumber(y, z)
x.print(x1)