class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        if x is None:
            return True
        
        p = []

        while x>0:

            p.append(x%10)
            x = x // 10
        
        if p == p[::-1]:
            return True
        else:
            return False

m = Solution()
print(m.isPalindrome(-120))
