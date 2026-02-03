class Solution:
    def isPalindrom(self, s:str)->str:
        m = len(s)
        # ababc

        def x(left:int, right:int)->int:

            while left >= 0 and right < m and s[left] == s[right]: #Explain what is going on here

                left -= 1
                right += 1

            return right - left -1
        
        maxL = 0
        current = 0

        for i in range(m):

            l1 = x(i , i)

            l2 = x(i, i+1)

            leng = max(l1 , l2)

            if leng > maxL:
                maxL = leng

                current = i - (leng - 1)//2 #explain what is going on here
        return s[current: current+maxL] #explain what is going on here
        
    
x1 = Solution()
x2 = x1.isPalindrom("ababc")
print(x2)