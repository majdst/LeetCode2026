class Solution:
    def reverse(self, s:list):
       # Conventional Method
        l = len(s)
        newL = []

        for i in range(l-1, -1, -1):
            newL.append(s[i])

        return newL
    
x = Solution()
y = x.reverse(["h","e","l","l","o"])
print(y)