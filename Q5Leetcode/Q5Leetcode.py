class Solution:
    def isPalindrom(self, s:str)->str:
        def rev(x:str) -> str:
           return x == x[::-1]
        l = len(s)
        maxL = ""

        for i in range(l):
           for j in range(i+1, l+1):
               substring = s[i:j]

               if rev(substring):
                   if len(substring) > len(maxL):
                       maxL = substring
        
        return maxL
        
    
x1 = Solution()
x2 = x1.isPalindrom("ababc")
print(x2)