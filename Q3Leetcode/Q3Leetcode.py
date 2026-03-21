class Solution:
    def leng(self, s:str)->int:
        
        #Brutforce method with TimeComplexity of O(n^3)
        l = len(s)
        max_l = 0

        for i in range(l): # O(n)
            for j in range(i+1, l+1): #O(n)
                substring = s[i:j] #O(n)
            
                if len(substring) == len(set(substring)):
                    max_l = max(max_l, len(substring))
        
        return max_l
    
    def longlen(self, s:str)->int:

        #SET method --> Time complexity O(n)
        l = len(s)
        max_l = 0
        left = 0
        n = set()

        for right in range(l):

            while s[right] in n:
                n.remove(s[left])
                left += 1
            
            n.add(s[right])

            max_l = max(max_l, right - left + 1)
        
        return max_l
    





mj = Solution()
print(mj.longlen("abcabcbb"))
