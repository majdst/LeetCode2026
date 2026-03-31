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

        lnght = 0
        curr = head
        while curr:
            lnght += 1
            curr = curr.next
        
        ln = lnght // k
        rem = lnght % k

        listL = []
        curr = head
        for i in range(k):
            listL.append(curr)
            size = ln + (1 if i < rem else 0)

            for j in range(size - 1):
                if curr:
                    curr = curr.next

            if curr:
                curr.next, curr = None, curr.next
        
        return listL

x = Solution()
l = x.helper([1,2,3,4,5,6,7,8,9,10])
y = x.print(l)
z = x.splitListToParts(l, 3)
print(z)

