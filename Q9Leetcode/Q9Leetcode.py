class Solution:
    def isPalindrome(self, x: int) -> bool:

       return str(x) == str(x)[::-1]
       

m = Solution()
print(m.isPalindrome(-121))
