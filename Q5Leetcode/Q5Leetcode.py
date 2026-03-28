class Solution:
    def isPalindrom(self, s:str)->str:
        #Brutforce method with the Time Complexity of O(n^3)
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
    def isPalindrom1(self, s:str)->str:
        #TimeComplexity of O(n^2)
        def x(y, left, right):
            while left >= 0 and right < len(y) and y[left]==y[right]:
                left -= 1
                right += 1

            return y[left+1: right]
        
        l = len(s)
        maxL = ""
        
        for i in range(l):

            odd = x(s, i, i)
            even = x(s, i, i+1)

            if len(odd) > len(maxL):
                maxL = odd
            if len(even) > len(maxL):
                maxL = even
            
        return maxL
        
    
x1 = Solution()
x2 = x1.isPalindrom("ababc")
print(x2)