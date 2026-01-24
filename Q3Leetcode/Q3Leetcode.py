class Solution:

    def lofLong(self, s:str) -> int:
        
        seen = set()
        max_l = 0
        l = 0
        m = len(s)

        for r in range(m):

            while s[r] in seen:

                seen.remove(s[l])

                l += 1

            seen.add(s[r])

            max_l = max(max_l, r - l + 1)

        return max_l    

mylist = Solution()
x1 = mylist.lofLong("abcabcb")

print(x1)