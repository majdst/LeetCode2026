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
x = Solution()
y = x.reverse1(["h","e","l","l","o"])
print(y)