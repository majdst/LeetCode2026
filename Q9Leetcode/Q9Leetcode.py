class Solution:
    def isPalindrome(self, x: int) -> bool:

       return str(x) == str(x)[::-1]
    
    def isPalindrome1(self, x: int) -> bool:

        if x < 0:
            return False
        remain, numb = 0, 0
        orig = x

        while x:
            remain = x % 10

            numb = numb * 10 + remain

            x //= 10
        
        return orig == numb
        
       

m = Solution()
print(m.isPalindrome1(121))
