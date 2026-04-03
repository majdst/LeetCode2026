class ListNode:
    def __init__(self, val= 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def help(self, nums:list)->ListNode:
        dummy = ListNode(0)
        current = dummy
        l = len(nums)

        for i in range(l):
            current.next = ListNode(nums[i])

            current = current.next
        
        return dummy.next
    def print(self, head:ListNode):
        current = head

        while current:
            print(f"{current.val} ->", end= "")
        
            current = current.next

    def numComponents(self, head:ListNode, nums:list)->int:
        newS = set(nums)
        current = head
        count = 0

        while current:
            if current.val in newS and (current.next is None or current.next.val not in newS):
                count += 1

            current = current.next
        
        return count
    
x = Solution()
y = x.help([0,1,2,3,4])
x.print(y)
print("")
print(x.numComponents(y, [0,1,3]))
