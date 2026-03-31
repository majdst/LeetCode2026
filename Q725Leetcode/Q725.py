class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def helper(self, s:list)->ListNode:

        l = len(s)
        dummy = ListNode(0)
        current = dummy

        for i in range(l):
            current.next = ListNode(s[i])
            current = current.next
        
        return dummy.next
    
    def print(self, s:ListNode):

        current = s
        while current:
            print(f'{current.val} -> ', end= "")
            current = current.next
        print('None')
    
    def splitListToParts(self, head:ListNode, k:int)->list:
        count = 0
        current = head

        while current:
            count += 1
            current = current.next
        
        ln = count // k
        rm = count % k

        current = head
        newL = []

        for i in range(k):
            newL.append(current)

            ln1 = ln + (1 if i < rm else 0)

            for _ in range(ln1 - 1):
                if current:
                    current = current.next

            if current:
                current.next, current = None, current.next
        
        return newL
x = Solution()
l = x.helper([1,2,3,4,5,6,7,8,9,10])
y = x.print(l)
z = x.splitListToParts(l, 3)
print(z)

