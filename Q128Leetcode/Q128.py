class Solution:
    def longestConsecutive(self, nums:list) ->int:

        newS = set(nums)
        maxL = 0

        for i in newS:

            if i - 1 not in newS:
                ln = 1

                while i + ln in newS:
                    ln += 1
            maxL = max(ln, maxL)
        
        return maxL
x = Solution()
print(x.longestConsecutive([100, 4, 200, 1, 3, 2]))

