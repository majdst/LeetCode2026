class Solution:
    def leng(self, s:str)->int:

        l = len(s)

        max_l = 0

        for i in range(l):
            for j in range(i+1, l+1):

                substring = s[i:j]

                if len(substring) == len(set(substring)):

                    max_l = max(max_l, len(substring))
        
        return max_l
    
mj = Solution()
print(mj.leng("abcdabcbb"))
