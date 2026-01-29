"""Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2."""

class Solution:
    def median(self, num1:list, num2:list)->int:

        x = num1 + num2

        x.sort()

        m = len(x)
        median = 0

        if m % 2 == 0:

            median = (x[m//2 - 1] + x[m//2]) * 0.5
        
        else:

            median = x[m//2]


        return median

y = Solution()
print(y.median([1,3], [2, 4]))

