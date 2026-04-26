class Solution:
    def reverse(self, s:list):
       # Conventional Method
        l = len(s)
        newL = []

        for i in range(l-1, -1, -1):
            newL.append(s[i])

        return newL
    def reverse1(self, s:list):
        l = len(s)
        left, right = 0, l-1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        return s
    def reverse2(self, s:list):
        l = len(s)
        def helper(x, left, right):
            #Stop sign
            if left >= right:
                return
            
            x[left], x[right] = x[right], x[left]

            return helper(x, left+1, right-1)
        
        helper(s, 0, l-1)
        return s
x = Solution()
y = x.reverse2(["h","e","l","l","o","M"])
print(y)