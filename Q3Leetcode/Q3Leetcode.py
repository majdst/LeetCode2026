class Solution:
    def leng(self, s:str)->int:

        l = len(s)
        seen = set()
        left = 0
        max_l = 0
        
        for right in range(l):
            if s[right] in seen:

                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_l = max(max_l, right - left + 1)

        
        return max_l
    
mj = Solution()
print(mj.leng("abcdabcbb"))
