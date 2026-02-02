class Solution:
    def long(self, s:str) -> str:

        def x(left:int, right:int)->int:

            while left >= 0 and right < len(s) and s[left] == s[right]:

                left -= 1
                right += 1

            return right -left - 1
        
        m = len(s)
        start = 0
        maxL = 0

        for i in range(m):

            l1 = x(i, i)

            l2 = x(i, i+1)

            currentL = max(l1, l2)

            if currentL > maxL:
                maxL = currentL
        
                start = i - (currentL-1)//2

        return s[start: start+maxL]

x1 = Solution()
print(x1.long("babad"))

        
